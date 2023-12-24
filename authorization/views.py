from django.shortcuts import render, redirect
from spotify import authorizate as auths

def render_login(request):#When user access the website
    try:
        if request.session['auth'] == True:
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
            return redirect('login')
        else:
            return redirect('login') 
    except KeyError:
        return redirect('login')

