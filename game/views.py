from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from playlists.models import Playlist, Song

@login_required
def game_board(request, playlist_id, slug):
    """ game """
    playlist = get_object_or_404(Playlist, pk=playlist_id, slug=slug, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)
    return render(request, 'game/game_board.html', {
        'playlist': playlist,
        'songs': songs,
    })
