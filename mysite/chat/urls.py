from django.urls import path

from . import views

# /chat/lobby
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
