from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('chat/<str:room_name>/', views.room_detail, name='room_detail'),
]
