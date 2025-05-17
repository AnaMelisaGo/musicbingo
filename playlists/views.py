from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddPlaylistForm, SongUploadForm
from .models import Playlist, Song


@login_required
def all_playlists(request):
    return render(request, 'playlists/includes/all_playlists.html', {})


@login_required
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
            return redirect('home')
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


@login_required
def edit_playlist(request, playlist_id, slug):
    """ To edit playlist and upload songs"""
    playlist = get_object_or_404(Playlist, pk=playlist_id, slug=slug, game_master=request.user)
    SongUploadFormset = modelformset_factory(Song, form=SongUploadForm, extra=0, can_delete=False)

    if request.method == 'POST':
        playlist_form = AddPlaylistForm(request.POST, instance=playlist)
        formset = SongUploadFormset(request.POST, request.FILES, queryset=Song.objects.filter(playlist=playlist))

        print("POST data:", request.POST)
        print("Files:", request.FILES)
        print("Formset cleaned data:")
        if playlist_form.is_valid() and formset.is_valid():
            playlist_form.save()
            formset_instances = formset.save(commit=False)

            for i, form in enumerate(formset.forms):
                song = form.instance
                clear_video = request.POST.get(f'clear_video_{i}') == 'true'
                if clear_video and song.video_file:
                    song.video_file.delete(save=False)
                    song.video_file = None
                if form.has_changed() or clear_video:
                    form.save()
                for song in formset_instances:
                    song.playlist = playlist
                    song.save()
            print(form.cleaned_data)
            messages.info(request, f'{playlist.name} is successfully updated!')
            return JsonResponse({'redirect_url': reverse('home')})
        else:
            messages.error(request, f'Error found')
            print("Formset errors:", formset.errors)
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        playlist_form = AddPlaylistForm(instance=playlist)
        formset = SongUploadFormset(queryset=Song.objects.filter(playlist=playlist))
    return render(request, 'playlists/edit_playlist.html', {
        'edit_playlist_page': True,
        'playlist': playlist,
        'playlist_form': playlist_form,
        'formset': formset,
    }
    )


@login_required   
def delete_playlist(request, playlist_id, slug):
    """ Delete playlist """
    playlist = get_object_or_404(Playlist, pk=playlist_id, slug=slug, game_master=request.user)
    playlist.delete()
    messages.success(request, f'Your playlist is deleted!')
    return redirect('home')
