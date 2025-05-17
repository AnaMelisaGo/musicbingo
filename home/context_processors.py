from playlists.models import Playlist


def global_context(request):
    """ A global context to pass the models accross the entire application """
    if request.user.is_authenticated:
        user_playlists = Playlist.objects.filter(game_master=request.user)
        return {
            'user_playlists': user_playlists,
            'can_add_playlist': user_playlists.count() < 5,
            }
    return {
        'user_playlists': [],
        'can_add_playlist': True,
    }