from django.shortcuts import render, redirect
from spotify import authorizate as auths

def render_login(request):   
    request.session['auth'] = False
    return render(request,'login.html')

def authorize(request):
    url = auths.authorize()
    return redirect(f'{url}')
