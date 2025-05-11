from django import forms
from .models import WatchedMovie


class WatchedMovieForm(forms.ModelForm):
    class Meta:
        model = WatchedMovie
        fields = ['movie', 'rating', 'review']
