from playlists.models import Playlist, Song


def global_context(request):
    """ A global context to pass the models accross the entire application """
    playlists = Playlist.objects.all()
    return {
        'playlists': playlists,
    }