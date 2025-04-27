from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    path('edit_playlist/<int:playlist_id>/<slug:slug>/', views.edit_playlist, name='edit_playlist'),
    path('delete_playlist/<int:playlist_id>/<slug:slug>/', views.delete_playlist, name='delete_playlist'),
]
