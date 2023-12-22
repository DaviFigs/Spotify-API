from django.shortcuts import render, redirect
from spotify import authortization as auths

def render_login(request):    
    return render(request, 'login.html')

def authorize(request):
    url = auths.authorize()
    return redirect(f'{url}')
