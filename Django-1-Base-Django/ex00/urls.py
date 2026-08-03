from django.urls import re_path
from . import views

urlpatterns = [
    # r'^ex00/?$' matches BOTH /ex00 and /ex00/, but nothing else
    # (so /ex00foo correctly falls through to a 404).
    re_path(r'^ex00/?$', views.index, name='ex00-index'),
]
