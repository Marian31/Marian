from django import forms
from .models import User, Album, Song


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = [""]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = [""]
        #fields


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = [""]



