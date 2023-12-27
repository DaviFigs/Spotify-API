import os
from dotenv import load_dotenv
load_dotenv()


def call_api( access_token, action, time):
    pass
    

def filtering(action, time):
    #type_options
    if action == '1':
        call_url = os.getenv('BASE_URL_TOP')+'/artists'



    access_token = request.session['access_token']
    headers = {
        'Authorization':'Bearer '+access_token
    }
    response = requests.get(os.getenv('BASE_URL')+'me', headers=headers)