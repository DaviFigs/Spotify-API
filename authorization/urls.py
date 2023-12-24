from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.render_login, name="login"),
    path('auth/', views.authorize, name='auth'),
    #path('exit_session/', views.exit_session, name="exit_session"),

]
