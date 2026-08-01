"""d05 URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Both with and without a trailing slash must work, and only these
    # exact URLs (no /ex00foo) must return a page.
    path('ex00', include('ex00.urls')),
    path('ex00/', include('ex00.urls')),
]
