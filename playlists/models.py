from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Playlist(models.Model):
    """ Model for Playlist """
    name = models.CharField(max_length=200, unique=True)
    game_master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        """ Display the playlist in ascending order according to the date created """
        ordering = ['created_on']

    def song_count(self):
        """ Function to count the number of songs in the playlist """
        return self.songs.count()

    def save(self, *args, **kwargs):
        """ Function to create slug to each playlist and pass them to the url for readability """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """ Function to return the name of the playlist and the Game Master """
        return f"{self.name} ({self.game_master.username})"


class Song(models.Model):
    """ Model for songs uploaded into the playlist """
    number = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(75)
        ]
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=200, blank=True, null=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='song')
    video_file = models.FileField(upload_to='video/', blank=True, null=True)

    def __str__(self):
        """ Function to return number and the title of the song """
        return f"{self.number} - {self.title}"
