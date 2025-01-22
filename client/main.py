from stream_handler import StreamHandler

from player import AudioPlayer
from essential_data import USER_GENDER, USER_NAME, ASSISTANT_NAME
from  program_settings import verbose, no_delete

transcriber_options = "asdfadfads"

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

    # Initialize and start the Recorder
    recorder = StreamHandler(audio_player=audio_player)
    recorder.start()

if __name__ == "__main__":
    main()