from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('main_app.urls')),
    path('authorization/', include('authorization.urls')),
    

]
