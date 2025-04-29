from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from playlists.models import Playlist, Song
from .models import Game
import random

@login_required
def start_gameboard(request, playlist_id, slug):
    """ Game board to play music bingo """
    playlist = Playlist.objects.get(pk=playlist_id, slug=slug, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)
    request.session['playlist_id'] = playlist_id
    request.session['called_numbers'] = []
    request.session['previous_numbers'] = []
    request.session['current_number'] = None
    request.session['prizes'] = ['Line Down', 'Line Across', 'Four Corners', 'Full House']
    request.session['available_prizes'] = []

    prizes = request.session.get('prizes', [])
    
    # game = Game.objects.create(game_master=request.user, playlist=playlist)
    return render(request, 'game/game_board.html', {
        'playlist': playlist,
        'songs': songs,
        'prizes': prizes,
    })


@login_required
def next_number(request):
    """ Function to scramble the numbers and push the numbers to the variables and
    pass them to the game board """

    if 'called_numbers' not in request.session:
        request.session['called_numbers'] = []

    playlist_id = request.session.get('playlist_id')
    playlist = Playlist.objects.get(pk=playlist_id, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)

    all_numbers = list(songs.values_list('number', flat=True))
    called_numbers = request.session.get('called_numbers', [])
    remaining_numbers = list(set(all_numbers) - set(called_numbers))
    current_number = request.session.get('current_number')

    #p = called_numbers[::-5]
    #previous_numbers = p[:-1]
    #current_number = None

    if remaining_numbers:
        next_number = random.choice(remaining_numbers)
        called_numbers.append(next_number)
        current_number = next_number
    #else

    return redirect('start_gameboard', playlist_id=playlist.id, slug=playlist.slug)

    """ 
    
    return render(request, 'game/game_board.html', {
            'called_numbers': called_numbers,
            'all_numbers': all_numbers,
            'previous_numbers': previous_numbers,
            'current_number': current_number,
        }) """
