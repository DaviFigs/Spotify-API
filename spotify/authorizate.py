import os
from dotenv import load_dotenv
load_dotenv()


def authorize(): #this function will authorize our app to take informations about the logged user
    auth_url = os.getenv('AUTHORIZE_URL')\
        +'?client_id='+os.getenv('CLIENT_ID')\
        +'&response_type=code'\
        +'&redirect_uri='\
        +os.getenv('CALLBACK_URL')\
        +'&show_dialog=true'\
        +'&scope=user-library-read user-top-read'\
        +'&state=wbfgiwgyretwe'
    return auth_url
