from django import forms
from .models import Winner

class AddWinnerForm(forms.ModelForm):
    """ To add new playlist """
    class Meta:
        model = Winner
        fields = ['name', 'prize', 'winning_numbers']
