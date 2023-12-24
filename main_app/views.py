from django.shortcuts import render, redirect
from spotify import settings as sett
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def callback(request):
    try:
        if request.session['auth'] == True:
            return redirect('main_page')
        else:
            response = sett.callbacks(code=request.GET.get('code'))
            request.session['auth'] = True
            request.session['access_token'] = response['access_token']
            return redirect('main_page')
    except:
        return redirect('login')
    
    
def main_page(request):
    try:
        if request.session['auth'] == True:
            access_token = request.session['access_token']
            headers = {
                'Authorization':'Bearer '+access_token
            }
            response = requests.get(os.getenv('BASE_URL')+'me', headers=headers)
            print(response.json())
            return render(request, 'callback.html')
        else:
            return redirect('login')    
    except:
        return redirect('login')
