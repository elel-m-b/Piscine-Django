from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^ex01/django/?$', views.django_page, name='ex01-django'),
    re_path(r'^ex01/display/?$', views.display_page, name='ex01-display'),
    re_path(r'^ex01/templates/?$', views.templates_page, name='ex01-templates'),
]
