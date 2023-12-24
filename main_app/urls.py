from django.urls import path
from . import views

urlpatterns = [
    path('callback/', views.callback, name="callback"),
    path('main_page/', views.main_page, name="main_page"),

]