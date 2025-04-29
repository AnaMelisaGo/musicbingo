from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('game_board/<int:playlist_id>/<slug:slug>/', views.start_game, name='start_game'),
    path('next_number/<int:playlist_id>/', views.next_number, name='next_number'),
]
