from django.shortcuts import render
from .forms import AddPlaylistForm, SongUploadForm

def playlists(request):
    """ To view playlist """
    playlists = True
    return render(request, 'playlists/edit_playlist.html', {
        'playlists': playlists,
    }
    )


def add_playlist(request):
    """ To add playlist and songs """
    if request.method == 'POST':
        playlist_form = AddPlaylistForm(request.POST)
        song_upload_form = SongUploadForm(request.POST)
        form = playlist_form and song_upload_form
        if form.is_valid:
            form.save()
            print(f'success')
        else:
            print(f'error')
    else:
        playlist_form = AddPlaylistForm()
        song_upload_form = SongUploadForm()
    template = 'playlists/add_playlist.html'
    context = {
        'playlist_form': playlist_form,
        'song_upload_form': song_upload_form,
    }
    return render(request, template, context)