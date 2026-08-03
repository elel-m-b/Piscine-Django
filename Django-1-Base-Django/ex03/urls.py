from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^ex03/?$', views.index, name='ex03-index'),
]
