from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.render_login, name="login"),
    path('authorize/', views.authorize, name="auth")

]
