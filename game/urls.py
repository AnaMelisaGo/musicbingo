from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('start_gameboard/<int:playlist_id>/<slug:slug>/', views.start_gameboard, name='start_gameboard'),
    path('next_number/', views.next_number, name='next_number'),
]
