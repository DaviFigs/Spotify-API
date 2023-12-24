from django.shortcuts import render, redirect
from spotify import authorizate as auths

def render_login(request):   
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def authorize(request):
    url = auths.authorize()
    return redirect(f'{url}')
