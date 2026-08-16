from django.urls import path
from . import views

urlpatterns = [
    path('init', views.init, name='ex08-init'),
    path('populate', views.populate, name='ex08-populate'),
    path('display', views.display, name='ex08-display'),
]
