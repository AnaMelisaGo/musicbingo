from playlists.models import Playlist


def global_context(request):
    """ A global context to pass the models accross the entire application """
    return {
        'playlists': Playlist.objects.all(),
    }