from django.shortcuts import render, redirect
from spotify import settings as sett
import requests
import os
from dotenv import load_dotenv
from django.contrib import messages
from django.contrib.messages import constants
from spotify import api_calls as api

load_dotenv()

def callback(request):#create session params and return him to main_page
    try:
        if request.session['auth'] == True:
            return redirect('main_page')
        else:
            response = sett.callbacks(code=request.GET.get('code'))
            request.session.set_expiry(3600)
            request.session['auth'] = True
            request.session['access_token'] = response['access_token']
            return redirect('main_page')
    except KeyError:
        messages.add_message(request, constants.ERROR, 'You have to login before access our application!')
        return redirect('login')
    

def main_page(request):
    try:
        if request.session['auth'] == True:
            messages.add_message(request, constants.SUCCESS, 'Hi, welcome to your spotify stats, your sesion will expire inside 1 hour, enjoy our application!!')
            return render(request, 'main.html')
        else:
            messages.add_message(request, constants.ERROR, 'You have to login before access our application!')
            return redirect('login')
    except KeyError:
        messages.add_message(request, constants.ERROR, 'You have to login before access our application!')
        return redirect('login')
    

def api_user_calls(request):
    action = request.GET.get('action')
    time = request.GET.get('time')
    access_token = request.session['access_token']
    limit = request.GET.get('limit')
    response = api.call_api(access_token,action,time,limit)
    print(response)

    return render(request,'main.html') 

