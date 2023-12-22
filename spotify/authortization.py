import os
from dotenv import load_dotenv
from .settings import main_string

load_dotenv()

def authorize():
    auth_url = os.getenv('AUTHORIZE_URL')+'?client_id='+os.getenv('CLIENT_ID')+'&response_type=code'+'&redirect_uri='+'http://127.0.0.1:8000/authorization/login/'+'&show_dialog=true'+'&escope=user-read-private user-read-email user-read-playback-state user-top-read'
    return auth_url

