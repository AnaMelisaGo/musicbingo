from django import forms
from .models import Playlist, Song


class AddPlaylistForm(forms.ModelForm):
    """ To add new playlist """
    class Meta:
        model = Playlist
        fields = ['name']


class SongUploadForm(forms.ModelForm):
    """ To upload songs to the playlist """
    video_file = forms.FileField(required=False, widget=forms.ClearableFileInput)
    class Meta:
        model = Song
        fields = ['number', 'title', 'artist', 'video_file']
