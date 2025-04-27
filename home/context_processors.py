from playlists.models import Playlist


def global_context(request):
    """ A global context to pass the models accross the entire application """
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(game_master=request.user)
        return {'playlists': playlists}
    return {
        'playlists': {},
    }