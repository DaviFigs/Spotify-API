import os
from dotenv import load_dotenv
import random
load_dotenv()


def authorize(): #this function will authorize our app to take informations about the logged user
    auth_url = os.getenv('AUTHORIZE_URL')\
        +'?client_id='+os.getenv('CLIENT_ID')\
        +'&response_type=code'\
        +'&redirect_uri='\
        +os.getenv('CALLBACK_URL')\
        +'&show_dialog=true'\
        +'&scope=user-library-read user-top-read'\
        +'&state='+create_random_string()
    return auth_url


def create_random_string():
    string = ''
    number = random.sample(range(1000), k=16)
    for i in number:
        string+=str(i)
    string = 'ILoveGiovana_'+string+'_MyEternalLove'#Yes,this is for my girl, devs always made it
    return string
    
