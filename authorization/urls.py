from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.render_login, name="login"),
    path('auth/', views.authorize, name='auth'),
    path('clearsession/', views.clearsession, name="clearsession"),

]
