from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.contrib import messages
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
        formset = SongUploadFormSet(request.POST, request.FILES, queryset=Song.objects.none())
        if playlist_form.is_valid() and formset.is_valid():
            playlist = playlist_form.save(commit=False)
            playlist.game_master = request.user
            playlist.save()
            songs = formset.save(commit=False)
            for song in songs:
                song.playlist = playlist # Assign the playlist to each song first
                song.save()
            
            messages.success(request, f'Your new playlist ({ playlist.name }) is successfully saved!')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, f'Something is wrong, please check!')
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


def edit_playlist(request, playlist_id, slug):
    """ To edit playlist and upload songs"""
    playlist = get_object_or_404(Playlist, pk=playlist_id, slug=slug)
    SongUploadFormset = modelformset_factory(Song, form=SongUploadForm, extra=0, can_delete=False)

    if request.method == 'POST':
        playlist_form = AddPlaylistForm(request.POST, instance=playlist)
        formset = SongUploadFormset(request.POST, request.FILES, queryset=Song.objects.filter(playlist=playlist))

        if playlist_form.is_valid() and formset.is_valid():
            playlist_form.save()
            formset.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        playlist_form = AddPlaylistForm(instance=playlist)
        formset = SongUploadFormset(queryset=Song.objects.filter(playlist=playlist))
    
    return render(request, 'playlists/edit_playlist.html', {
        'playlist_page': True,
        'playlist': playlist,
        'playlist_form': playlist_form,
        'formset': formset,
    }
    )