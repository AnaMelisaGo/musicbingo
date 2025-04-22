from django.contrib import admin
from .models import Playlist, Song

class SongInLine(admin.TabularInline):
    """ To manage each playlists through admin """
    model = Song
    extra = 1

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    """ To add or edit songs directly from admin """
    inlines = [SongInLine]