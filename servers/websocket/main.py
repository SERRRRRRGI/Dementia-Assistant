from transcriber import Transcriber, transcriber_utils
from stream_handler import StreamHandler
from handler import Handler
from main_assistant import MainAssistant
from player import AudioPlayer

from essential_data import USER_GENDER, USER_NAME, ASSISTANT_NAME
from  program_settings import verbose, no_delete

from server import socket

transcriber_options = {
    "language": "ca",
    "prompt": transcriber_utils.generate_prompt(user_name=USER_NAME, user_gender=USER_GENDER, assistant_name=ASSISTANT_NAME)
}

def main():
    # Print welcome message and settings
    print(f"\033[95m===DIGUES HOLA A {ASSISTANT_NAME}, EL TEU ASSISTENT DE VEU INTEL·LIGENT===\033[0m\n")

    #print program settings information
    if verbose:
        print("\033[93mVerbose Mode:\033[0m \033[92mON\033[0m")
    else:
        print("\033[93mVerbose Mode:\033[0m \033[91mOFF\033[0m")
    
    if no_delete:
        print("\033[93mNo Delete Mode:\033[0m \033[92mON\033[0m")
    else:
        print("\033[93mNo Delete Mode:\033[0m \033[91mOFF\033[0m")

    print("")

    #initialize player
    audio_player = AudioPlayer()

    #initialize assistant
    main_assistant = MainAssistant(name=ASSISTANT_NAME, audio_player=audio_player)

    #initialize the transcription handler
    handler= Handler(assistant=main_assistant)

    # Initialize the Transcriber
    transcriber = Transcriber()

    # Initialize and start the Recorder
    recorder = StreamHandler(transcriber=transcriber, transcriber_options=transcriber_options, result_handler=handler, audio_player=audio_player)
    recorder.start()    

if __name__ == "__main__":
    main()