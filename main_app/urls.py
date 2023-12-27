from django.urls import path
from . import views

urlpatterns = [
    path('callback/', views.callback, name="callback"),
    path('main_page/', views.main_page, name="main_page"),
    path('api_calls/', views.api_user_calls, name="api_calls"),
    

]