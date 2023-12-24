from django.shortcuts import render
from spotify import settings as sett
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def callback(request):
    code = request.GET.get('code')
    response = sett.callbacks(code=code)
    print(response)
    access_token = response['access_token']

    headers = {
        'Authorization':'Bearer '+access_token
    }
    response1 = requests.get(os.getenv('BASE_URL')+'me', headers=headers)
    print(response1.json())

    
    return render(request, 'callback.html')

