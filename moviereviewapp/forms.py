from django import forms
from .models import Movie, MovieType, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'