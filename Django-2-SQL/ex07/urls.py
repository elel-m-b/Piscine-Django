from django.urls import path
from . import views

urlpatterns = [
    path('populate', views.populate, name='ex07-populate'),
    path('display', views.display, name='ex07-display'),
    path('update', views.update, name='ex07-update'),
]
