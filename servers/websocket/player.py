import queue
import tempfile
import soundfile as sf
import numpy as np
import os
from threading import Thread

from openai_client import OPENAI_CLIENT

from  program_settings import verbose, no_delete
from stream_constants import SampleRate, BlockSize

from server import socket

class AudioPlayer:
    def __init__(self):

        self.client = OPENAI_CLIENT

        self.stop_flag=False
        self.playing = False

        self.output_queue=queue.Queue()
        self.output_buffer=np.zeros((int(SampleRate * BlockSize / 1000), 1), dtype=np.float32)

        self.temp = tempfile.NamedTemporaryFile(prefix="player_", suffix=".wav", delete=False)

        if no_delete: print("\nNew player temp file: ", self.temp.name)

    def _restart_temp_file(self):
        self.temp.close()

        # Make sure to delete the temporary file when done
        try:
            if not no_delete: os.remove(self.temp.name)
        except Exception as e:
            print(f"Could not delete temp file: {e}") 
        finally:
            self.temp=tempfile.NamedTemporaryFile(prefix="player_", suffix=".wav", delete=False)
            if no_delete: print("\nNew player temp file: ", self.temp.name)


    def _play(self, file_path):
        self._stop()
        self.stop_flag = False
        self.playing = True
        blocksize=BlockSize

        with sf.SoundFile(file_path, mode="r") as file:
            for block in file.blocks(blocksize=blocksize, dtype="float32"):  # Read audio in chunks (frames)
                if self.stop_flag:
                    break  # Stop playback if stop flag is triggered
                else:
                    self.playing = True

                # Check the number of dimensions
                if len(block.shape) == 1:
                    # If 1D array, convert to 2D with one channel
                    block = block.reshape(-1, 1)
                elif len(block.shape) == 2:
                    # If 2D array, ensure it has one column
                    if block.shape[1] != 1:
                        block = block[:, :1]
                else:
                    raise ValueError("Unexpected block shape: {}".format(block.shape))

                # If block has fewer frames than expected, pad it with zeros
                if block.shape[0] < blocksize:
                    padding = np.zeros((blocksize - block.shape[0], block.shape[1]), dtype='float32')
                    block = np.vstack((block, padding))  # Combine the block and padding

                # Put reshaped block into queue
                socket.emit("outdata", to=socket.indata_sender,outdata=block)

        self.playing = False


    def _stop(self):
        self.stop_flag = True
        #clearing the queue
        with self.output_queue.mutex:
            self.output_queue.queue.clear()

        self.playing = False
        
        socket.emit("stop_audio", socket.indata_sender)
        
    def _tts_and_play(self, text, voice="alloy", speed=1):
        self._stop()
        self.stop_flag = False
        self._restart_temp_file()

        if verbose: print("generating audio...")
        response = self.client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text,
            response_format="wav",
            speed=speed
        )

        response.stream_to_file(self.temp.name)

        if verbose: print("audio generated! PLAYING: ", self.temp.name)

        self._play(self.temp.name)

    def stop(self):
        #if not self.playing: return
        thread=Thread(daemon=True, name="AIAssistant_stop_playing", target=self._stop)
        thread.start()
        return thread
    
    def play(self, file_path):
        thread=Thread(daemon=True, name="AIAssistant_play_audio", target=self._play, args=(file_path,))
        thread.start()
        return thread

    def tts_and_play(self, text, voice="nova", speed=1):
        thread=Thread(daemon=True, name="AIAssistant_TTS_and_play", target=self._tts_and_play, args=(text, voice, speed))
        thread.start()
        return thread