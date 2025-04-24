from django import forms
from .models import Playlist, Song
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class AddPlaylistForm(forms.ModelForm):
    """ To add new playlist """
    class Meta:
        model = Playlist
        fields = ['name']


class SongUploadForm(forms.ModelForm):
    """ To upload songs to the playlist """
    class Meta:
        model = Song
        fields = ['number', 'title', 'artist', 'video_file']
