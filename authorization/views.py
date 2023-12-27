from django.shortcuts import render, redirect
from spotify import authorizate as auths
from django.contrib.messages import constants
from django.contrib import messages



def render_login(request):#When user access the website
    try:
        if request.session['auth'] == True:
            messages.add_message(request, constants.WARNING, 'Sorry, you are already on a session')
            return redirect('main_page')
        else:
            request.session['auth'] = False
            return render(request,'login.html')
        
    except KeyError:
        request.session['auth'] = False
        return render(request, 'login.html')

def authorize(request):#This is an api call, this url return user to callback function
    url = auths.authorize()
    return redirect(f'{url}')


def clearsession(request):
    try:
        if request.session['auth'] == True:
            request.session.flush()
            messages.add_message(request, constants.INFO, 'Thak you for use our application, hope you were enjoying!')
            return redirect('login')
        else:
            messages.add_message(request,constants.ERROR, 'You have to login before access our application!')
            return redirect('login') 
    except KeyError:
        messages.add_message(request,constants.ERROR, 'You have to login before access our application!')
        return redirect('login')

