"""
URL configuration for the d05 project.

Every exercise application defines its own URLs (see each app's urls.py,
as required by the subject) and is simply plugged in here.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ex00.urls')),
    path('', include('ex01.urls')),
    path('', include('ex02.urls')),
    path('', include('ex03.urls')),
]
