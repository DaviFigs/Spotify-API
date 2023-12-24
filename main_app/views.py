from django.shortcuts import render
from spotify import settings as sett

def callback(request):
    code = request.GET.get('code')
    print(code)
    response = sett.get_user_information(code)
    print(response.json())
    
    return render(request, 'callback.html')

