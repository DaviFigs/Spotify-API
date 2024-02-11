from django.shortcuts import render, redirect
from spotify import settings as sett
from dotenv import load_dotenv
from django.contrib import messages
from django.contrib.messages import constants
from spotify import api_calls as api

load_dotenv()

def redirect_home(request):
    return redirect('login') 

def callback(request):#This url receive a json data
    try:
        if request.session['auth'] == True:
            return redirect('main_page')
        else:
            code = request.GET.get('code')
            response = sett.callbacks(code)#This function will give us the access token
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
            return render(request, 'main.html')
        else:
            messages.add_message(request, constants.ERROR, 'You have to login before access our application!')
            return redirect('login')
    except KeyError:
        messages.add_message(request, constants.ERROR, 'You have to login before access our application!')
        return redirect('login')
    

from spotify.json_manager import json_decript as jsp

def api_user_calls(request):
    try:
        if request.session['auth'] == False:
            messages.add_message(request, constants.WARNING, 'You have to login before access our application!')
            return redirect('login')
        else:
            try:
                action = request.GET.get('action')
                time = request.GET.get('time')
                access_token = request.session['access_token']
                limit = request.GET.get('limit')

                response = api.call_api(access_token,action,time,limit)#SPOTIFY API CALL

                message = api.create_message(action, time, limit)#create one especific message for user

                if action == '1':
                    artist_list = jsp.get_artists_info(response)
                    context = {
                        'artists':artist_list,
                        'message':message
                    }
                elif action == '2':
                    tracks_list = jsp.get_tracks_info(response)
                    context ={
                        'tracks':tracks_list,
                        'message':message
                    }

                return render(request,'main.html', context=context) 
            except:
                messages.add_message(request, constants.WARNING, 'Sorry, something is wrong, is not your fault')
                return redirect('main_page')
    except Exception as e:
        messages.add_message(request, constants.WARNING, f'Error: {e}, your session expired!')
        return redirect('login')