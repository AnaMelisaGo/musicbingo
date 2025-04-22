from django import forms
from .models import Playlist, Song

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

    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(1, 76):
            field_name: f'number_{i}'
            self.fields[field_name] = forms.IntegerField(
                label=f'Number',
                initial=i,
                min_value=1,
                max_value=75,
            ) """

