from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^ex02/?$', views.index, name='ex02-index'),
]
