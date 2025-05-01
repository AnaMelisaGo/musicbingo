from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('start_gameboard/<int:playlist_id>/<slug:slug>/', views.start_gameboard, name='start_gameboard'),
    path('next_number/', views.next_number, name='next_number'),
    path('music_bingo/', views.music_bingo, name='music_bingo'),
    path('add_winner/', views.add_winner, name='add_winner'),
]
