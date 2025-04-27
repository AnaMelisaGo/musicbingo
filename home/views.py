from django.shortcuts import render
from playlists.models import Playlist

# Create your views here.
def index(request):
    """ View to return the index page """
    playlists = Playlist.objects.all()
    context = {
        'playlists': playlists
    }
    print('context is:', context)
    return render (request, 'home/index.html', context)
