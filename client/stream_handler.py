import sounddevice as sd
#import soundfile as sf
import queue
import os
import numpy as np
import tempfile
from threading import Thread


from  program_settings import verbose, no_delete

from essential_data import USER_GENDER, USER_NAME, ASSISTANT_NAME

from stream_constants import Vocals, SampleRate, BlockSize, EndBlocks, FlushBlocks, ConnectionBlocks

from client import socket

transcriber_options = "sf"


class AudioBuffer:
    def __init__(self, number):
        self.number = number

        self.buffer = queue.Queue()
        self.temp = tempfile.NamedTemporaryFile(prefix="recorder_",suffix=".wav", delete=False)
        self.file = "df" #sf.SoundFile(self.temp.name, mode='w', samplerate=SampleRate, channels=1)
        self.opened_file = None

        self.blocks_speaking = FlushBlocks

        self.context_prompt = None
        self.continuation = False

        if no_delete: print("\nNew audio buffer file: ", self.temp.name)

    def save_to_file(self):
        for _ in range(0, self.buffer.qsize()):
            self.file.write(self.buffer.get())
            if verbose: print("|", end="", flush=True)

    
    def put(self, data):
        self.buffer.put(data)
        self.blocks_speaking -= 1
    
    def get_file_content(self):
        self.save_to_file()
        self.opened_file = open(self.temp.name, "rb")
        return self.opened_file

    def terminate(self):
        if self.opened_file:
            self.opened_file.close()

        self.file.close()
        self.temp.close()
        # Make sure to delete the temporary file when done
        try:
            if not no_delete: os.remove(self.temp.name)
        except Exception as e:
            print(f"Could not delete temp file: {e}")


class StreamHandler:
    def __init__(self, audio_player, threshold=0.01, input_device=None, output_device=None, contaminated_streams=False):
        self.contaminated_streams = contaminated_streams

        self.threshold = threshold
        self.input_device = input_device
        self.output_device=output_device

        self.audio_player = audio_player
        
        self.running = True
        self.waiting = 0
        self.buffers = [AudioBuffer(number=0), AudioBuffer(number=1), AudioBuffer(number=2)]
        self.buffer_counter = 2
        self.speaking = False
        self.blocks_speaking = 0
        self.buffers_to_process = []

        self.transcriber_options = transcriber_options


    def _is_there_voice(self, indata, frames):
        freq = np.argmax(np.abs(np.fft.rfft(indata[:, 0]))) * SampleRate / frames
        volume = np.sqrt(np.mean(indata**2))

        return volume > self.threshold and Vocals[0] <= freq <= Vocals[1]
    
    # method to pop and populate buffer array at once
    def _pop_buffer(self, number):
        poped_buffer=self.buffers.pop(number)

        #creating new buffer on index 1
        self.buffers.append(AudioBuffer(number=self.buffer_counter))
        self.buffer_counter+=1

        return poped_buffer
    
    def _save_to_process(self, continuation=False):

        self.buffers[0].continuation = continuation
        self.speaking = continuation

        #sending and deliting current buffer
        current_buffer=self._pop_buffer(0)
        self.buffers_to_process.append(current_buffer)

        if not continuation:
            self._pop_buffer(0)

    def _save_to_buffer(self, indata, isThereVoice=False):
        def sendIndata():
            socket.emit("indata", indata=indata, isThereVoice=isThereVoice)
        
        Thread(target=sendIndata, name="Send indata", daemon=True).start()

    def callback(self, indata, outdata, frames, _time, status):

        # Omplir outdata amb l'àudio que es vol reproduir
        try:
            data = self.audio_player.output_queue.get_nowait()
            outdata[:] = data
            # Actualitzar audio_player.output_buffer per a cancel·lació
            self.audio_player.output_buffer[:frames, :] = data

        except queue.Empty:
            outdata.fill(0)
            self.audio_player.output_buffer.fill(0)

        if not any(indata):
            return
        
        if self.contaminated_streams:
            # Restar l'àudio de sortida de l'entrada per cancel·lar l'eco
            indata = indata - self.audio_player.output_buffer[:frames, :]

        voice = self._is_there_voice(indata, frames)

        if not voice and not self.speaking:
            return
        
        if voice:  # User speaking
            if verbose:
                print(".", end="", flush=True)

            self._save_to_buffer(indata, True)
            self.waiting = EndBlocks

            self.speaking = True
        else:  # Silence after user has spoken
            self.waiting -= 1
            if self.waiting < 0:
                self.speaking = False
                return
            else:
                if verbose:
                    print("-", end="", flush=True)
                
                self._save_to_buffer(indata, False)

    def process(self):
        if len(self.buffers_to_process) > 0:
            buffer: AudioBuffer = self.buffers_to_process.pop(0)
            file = buffer.get_file_content()
            if verbose:
                print("\n\033[90mTranscribing..\033[0m")

            #generating correct transcription prompt
            prompt = self.transcriber_options["prompt"] or ""
            if buffer.context_prompt:
                prompt += " " + buffer.context_prompt

            result = self.transcriber.transcribe(
                audio_data=file,
                language=self.transcriber_options["language"] or "ca",
                prompt=prompt,
                continuation=buffer.continuation,
            )

            buffer.terminate()

            if not buffer.continuation:
                if verbose: print(f"\033[1A\033[2K\033[0G{result}")
                else:
                    print("")
            
                self.result_handler.handle(result, speaker=USER_NAME)
            elif buffer.number + 1 == self.buffers[0].number:

                #split the string in the best way possible in order for it to be between 5 and 30 characters
                context = result.split(".")[-1]
                if len(context) > 30 or len(context) < 5:
                    context = result.split(",")[-1]
                if len(context) > 30 or len(context) < 5:
                    context = result[-30:]

                self.buffers[0].context_prompt = context

    def listen(self):
        # Get the default input and output devices
        input_device = sd.default.device[0] if sd.default.device[0] is not None else None
        output_device = sd.default.device[1] if sd.default.device[1] is not None else None

        # If you have specific devices set, use them; otherwise, use defaults
        show_input_device = input_device if input_device is not None else sd.default.device[0]
        show_output_device = output_device if output_device is not None else sd.default.device[1]

        # Print device information
        print(f"\033[32mLive input device: \033[37m{sd.query_devices(device=show_input_device)['name']}\033[0m")
        print(f"\033[32mLive output device: \033[37m{sd.query_devices(device=show_output_device)['name']}\033[0m")
        print("\033[32mListening.. \033[37m(Ctrl+C to Quit)\033[0m")

        with sd.Stream(
            channels=1,
            callback=self.callback,
            blocksize=BlockSize,
            samplerate=SampleRate,
            device=self.input_device,
        ):
            while self.running:
                for buffer in self.buffers:
                    buffer.save_to_file()
                
                Thread(target=self.process, name="AIAssistant_processing_audio", daemon=True).start()

    def start(self):
        try:
            self.listen()
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            print("\n\033[93mQuitting..\033[0m")