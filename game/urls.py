from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('game_board/<int:playlist_id>/<slug:slug>/', views.game_board, name='game_board'),
]
