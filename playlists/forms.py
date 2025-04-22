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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('number', css_class='col-md-2'),
                Column('title', css_class='col-md-4'),
                Column('artist', css_class='col-md-4'),
                Column('video_file', css_class='col-md-2'),
            )
        )

    """ 

        for i in range(1, 76):
            field_name: f'number_{i}'
            self.fields[field_name] = forms.IntegerField(
                label=f'Number',
                initial=i,
                min_value=1,
                max_value=75,
            ) """

