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
    request.session['prizes_claimed'] = []

    prizes = request.session.get('prizes', [])
    
    # game = Game.objects.create(game_master=request.user, playlist=playlist)
    return render(request, 'game/game_board.html', {
        'playlist': playlist,
        'songs': songs,
        'prizes': prizes,
        'game_board': True
    })


@login_required
def next_number(request):
    """ Function to scramble the numbers and push the numbers to the variables """

    if 'called_numbers' not in request.session:
        request.session['called_numbers'] = []

    playlist_id = request.session.get('playlist_id')
    playlist = Playlist.objects.get(pk=playlist_id, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)

    all_numbers = list(songs.values_list('number', flat=True))
    called_numbers = request.session.get('called_numbers', [])
    remaining_numbers = [num for num in all_numbers if num not in called_numbers]
    current_number = request.session.get('current_number')
    previous_numbers = request.session.get('previous_numbers', [])

    if not isinstance(called_numbers, list):
        called_numbers = []

    if remaining_numbers:
        next_number = random.choice(remaining_numbers)
        called_numbers.append(next_number)
        current_number = next_number
        

    #else

    #update session variables
    request.session['called_numbers'] = called_numbers
    request.session['current_number'] = current_number
    request.session['previous_numbers'] = called_numbers[-2:-7:-1]
    request.session.modified = True

    print('Called numbers:', request.session.get('called_numbers'))
    print(f'this are all numbers {all_numbers}')
    return redirect('music_bingo')


@login_required
def music_bingo(request):
    playlist_id = request.session.get('playlist_id')
    playlist = Playlist.objects.get(pk=playlist_id, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)
    called_numbers = request.session.get('called_numbers')
    current_number = request.session.get('current_number')
    previous_numbers = request.session.get('previous_numbers')
    current_song = songs.filter(number=current_number).first()
    prizes = request.session.get('prizes')
    prizes_claimed = request.session.get('prizes_claimed')
    context = {
        'called_numbers': called_numbers,
        'current_number': current_number,
        'previous_numbers': previous_numbers,
        'playlist': playlist,
        'songs': songs,
        'current_song': current_song,
        'game_board': False,
        'prizes': prizes,
        'prizes_claimed': prizes_claimed
    }

    return render(request, 'game/game_board.html', context)
