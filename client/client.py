from dotenv import load_dotenv
load_dotenv()

import os
import socketio
import numpy as np
from utils.io import encode_data, decode_data  # Import the utility functions
from threading import Thread

# Event listener for receiving a response from the server
def on_audio_response(encoded_data):
    # Decode the msgpack response data
    decoded_data = decode_data(encoded_data)
    audio_array = decoded_data['audio_array']
    is_there_voice = decoded_data['isThereVoice']
    
    print('Received audio array from server:', audio_array)
    print('Is there voice (response):', is_there_voice)

# Example NumPy array representing audio data
audio_array = np.array([[0.5, 1.0, 0.75], [0.8, 0.9, 0.6]], dtype=np.float64)
is_there_voice = True  # Example variable indicating presence of voice

# Encode the audio array and the isThereVoice flag using msgpack
encoded_data = encode_data(audio_array=audio_array, isThereVoice=is_there_voice)

class SocketClient:

    def __init__(self, url, auth_token):
        self.sio = socketio.Client()

        # Connect to the server
        self.sio.connect(url, auth={
            "token": auth_token
        })
        
        
        
        self.sio.on("connect", self.connect_handler)

        Thread(target=self.sio.wait, name="wait for WS requests").start()
    
    def connect_handler(_):
            print("Connected to WS server succesfully!")

    def on(self, event_name, event_handler):
        def handler(encoded_data):
            decoded_data = decode_data(encoded_data)
            event_handler(decoded_data)
        
        self.sio.on(event_name, handler)

    def emit(self, event_name, **kwargs):
        encoded_data = encode_data(**kwargs)
        self.sio.emit(event_name, encoded_data)

socket = SocketClient(url=os.environ.get('WS_URL'), auth_token=os.environ.get("WS_AUTH_TOKEN"))