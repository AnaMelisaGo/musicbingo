from django.db import models
from django.contrib.auth.models import User
from playlists.models import Playlist


class Game(models.Model):
    """ Game model """
    played_on = models.DateTimeField(auto_now_add=True)
    game_master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    called_numbers = models.JSONField(default=list)

    class Meta:
        """ Display the playlist in ascending order according to the date created """
        ordering = ['-played_on']

    def __str__(self):
        """ Function to return the dates of the game played and the game_master """
        return f"Played {self.playlist} on {self.played_on} by {self.game_master}"


class Winner(models.Model):
    """ Winner model """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='winner')
    name = models.CharField(max_length=255)
    prize = models.CharField(max_length=255)
    winning_numbers = models.JSONField(default=list)

    def __str__(self):
        """ Return the name and prize of the winner """
        return f'The winner for {self.prize} is {self.name}!'