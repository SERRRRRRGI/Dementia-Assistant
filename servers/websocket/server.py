from dotenv import load_dotenv
load_dotenv()

import os

import socketio
import numpy as np
from threading import Thread
from flask import Flask

from utils.io import encode_data, decode_data  # Import the utility functions
from auth import authenticate_token

class SocketServer:
    def __init__ (self, port=5000):
        # Create a Socket.IO server
        self.sio = socketio.Server()

        # Flask app to host the socket.io server
        self.app = Flask(__name__)
        self.app.wsgi_app = socketio.WSGIApp(self.sio, self.app.wsgi_app)

        self.port = port or 5000

        #Event listener for connect
        self.sio.on("connect", self.connect_handler)
        # Event listener for disconnect
        self.sio.on("disconnect", self.disconnect_handler)


        #other properties
        self.indata_sender=None

    def _authenticate_token(self, token):
        return authenticate_token(token)
    
    def connect_handler(self, sid, environ, auth):
        # Extract token from the HTTP headers
        token = auth.get('token')

        if token and self._authenticate_token(token):
            print('Client connected:', sid)
            self.indata_sender = sid
        else:
            print('Unauthorized connection attempt from:', sid)
            self.sio.disconnect(sid)  # Disconnect unauthorized clients
    
    def disconnect_handler(self, sid):
        print('Client disconnected:', sid)
    
    def _run(self):
        thread = Thread(target=self.app.run, kwargs={"port": self.port, "host": "0.0.0.0"}, name="WS Server", daemon=True)
        thread.start()

        return thread
    
    def run(self):
        return self._run()
    
    def on(self, event_name, event_handler):
        def handler(sid, encoded_data):
            decoded_data = decode_data(encoded_data)
            event_handler(sid, decoded_data)
        
        self.sio.on(event_name, handler)

    def emit(self, event_name, to=None, room=None, **kwargs):
        encoded_data = encode_data(**kwargs)
        self.sio.emit(event_name, encoded_data, to=to, room=room)



socket = SocketServer(port=os.getenv("PORT"))