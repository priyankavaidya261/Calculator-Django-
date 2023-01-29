from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('new/',include('calapp.urls')),
    path('admin/', admin.site.urls),
]
