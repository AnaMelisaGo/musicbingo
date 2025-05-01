from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from playlists.models import Playlist, Song
from django.contrib import messages
from .models import Game
from .forms import AddWinnerForm
import random
import json

@login_required
def start_gameboard(request, playlist_id, slug):
    """ Game board to play music bingo and create the game to store data"""
    playlist = Playlist.objects.get(pk=playlist_id, slug=slug, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)
    request.session['playlist_id'] = playlist_id
    request.session['called_numbers'] = []
    request.session['previous_numbers'] = []
    request.session['current_number'] = None
    request.session['prizes'] = ['Line Down', 'Line Across', 'Four Corners', 'Full House']
    request.session['prizes_claimed'] = []

    request.session['winner_name'] = None
    request.session['winner_prize'] = None
    request.session['winning_numbers'] = []
    request.session['winner'] = False
    
    # game = Game.objects.create(game_master=request.user, playlist=playlist)
    return render(request, 'game/game_board.html', {
        'playlist': playlist,
        'songs': songs,
        'prizes': request.session.get('prizes', []),
        'game_board': True
    })


@login_required
def next_number(request):
    """ Function to scramble the numbers and push the numbers to the variables """

    if 'called_numbers' not in request.session:
        request.session['called_numbers'] = []

    winner = request.session.get('winner')
    if winner:
        request.session['winner'] = False
        request.session['winner_name'] = None
        request.session['winner_prize'] = None
        request.session['winning_numbers'] = []

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
def add_winner(request):
    """ Function to add winner in the session and create the model to store data of the winner """
    prizes = request.session.get('prizes')
    prizes_claimed = request.session.get('prizes_claimed', [])

    if request.method == 'POST':
        numbers_json = request.POST.get('selected_numbers')
        numbers = json.loads(numbers_json) if numbers_json else []

        name = request.POST.get('name')
        prize = request.POST.get('prize')

        prizes_claimed.append(prize)
        request.session['winner_name'] = name
        request.session['prize'] = prize
        request.session['winning_numbers'] = numbers
        request.session['prizes_claimed'] = prizes_claimed
        request.session['winner'] = True

        available_prizes = [p for p in prizes if p not in prizes_claimed]
        messages.warning(request, f'Available prizes to win : {available_prizes}')
        print(request.session.get('prizes_claimed'))

    return redirect('music_bingo')


@login_required
def music_bingo(request):
    playlist_id = request.session.get('playlist_id')
    playlist = Playlist.objects.get(pk=playlist_id, game_master=request.user)
    songs = Song.objects.filter(playlist=playlist)
    current_number = request.session.get('current_number')
    current_song = songs.filter(number=current_number).first()
    called_numbers = request.session.get('called_numbers',[])
    called_num = sorted(called_numbers)
    prizes_claimed = request.session.get('prizes_claimed', [])
    prizes = request.session.get('prizes')
    print(f'these are prizes: {len(prizes)}, these are claimed: {len(prizes_claimed)}')

    context = {
        'called_numbers': called_numbers,
        'called_num': called_num,
        'previous_numbers': request.session.get('previous_numbers', []),
        'current_number': current_number,
        'playlist': playlist,
        'songs': songs,
        'current_song': current_song,
        'game_board': False,
        'prizes': prizes,
        'prizes_claimed': prizes_claimed,
        'winner': request.session.get('winner'),
        'winner_name': request.session.get('winner_name'),
        'winner_prize': request.session.get('winner_prize'),
        'winning_numbers': request.session.get('winning_numbers', []),
    }

    return render(request, 'game/game_board.html', context)


def end_game(request):
    """ End the music game """
    # needs fixing
    request.session.flush()
    return redirect('home')