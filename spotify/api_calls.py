import os
from dotenv import load_dotenv
load_dotenv()


'''
    access_token = request.session['access_token']
    headers = {
        'Authorization':'Bearer '+access_token
    }
    response = requests.get(os.getenv('BASE_URL')+'me', headers=headers)
    '''