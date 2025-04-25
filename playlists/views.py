from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import AddPlaylistForm, SongUploadForm
from .models import Playlist, Song


def all_playlists(request):
    """ To view playlist """
    playlists = Playlist.objects.all()
    return render(request, 'base.html', {
        'playlist_page': True,
        'playlists': playlists,
    }
    )


def add_playlist(request):
    """ To add playlist and songs """
    SongUploadFormSet = modelformset_factory(Song, form=SongUploadForm, extra=75, can_delete=False)
    
    if request.method == 'POST':
        playlist_form = AddPlaylistForm(request.POST)
        formset = SongUploadFormSet(request.POST, queryset=Song.objects.none())
        if playlist_form.is_valid() and formset.is_valid():
            playlist_form.save()
            formset.save()
            # add a message success
            return redirect('home')
        else:
            print('error')
    else:
        playlist_form = AddPlaylistForm()
        initial_data = [{'number':i} for i in range(1, 76)]
        formset = SongUploadFormSet(queryset=Song.objects.none(), initial=initial_data)
    template = 'playlists/add_playlist.html'
    context = {
        'playlist_form': playlist_form,
        'formset': formset,
        'playlist_page': True,
    }
    return render(request, template, context)


def edit_playlist(request):
    """ To view playlist """
    playlists = Playlist.objects.all()
    return render(request, 'playlists/edit_playlist.html', {
        'playlist_page': True,
        'playlists': playlists
    }
    )