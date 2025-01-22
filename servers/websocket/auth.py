from dotenv import load_dotenv
load_dotenv()

import os

def authenticate_token(token):
    AUTH_TOKEN = os.environ.get('WS_AUTH_TOKEN')
    
    return token == AUTH_TOKEN