from django import forms
from .models import WatchedMovie, Movie

class WatchedMovieForm(forms.ModelForm):
    class Meta:
        model = WatchedMovie
        fields = ['movie', 'rating', 'review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie'].queryset = Movie.objects.all().order_by('title')
        self.fields['movie'].label_from_instance = lambda obj: f"{obj.title} ({obj.release_year}) - {obj.genre}"

