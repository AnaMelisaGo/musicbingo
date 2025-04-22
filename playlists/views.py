from django.shortcuts import render

def playlists(request):
    """ To view playlist """
    playlists = True
    return render(request, 'playlists/edit_playlist.html', {
        'playlists': playlists,
    }
    )