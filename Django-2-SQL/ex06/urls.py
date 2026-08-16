from django.urls import path
from . import views

urlpatterns = [
    path('init', views.init, name='ex06-init'),
    path('populate', views.populate, name='ex06-populate'),
    path('display', views.display, name='ex06-display'),
    path('update', views.update, name='ex06-update'),
]
