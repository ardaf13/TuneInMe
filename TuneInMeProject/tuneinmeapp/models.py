from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    poster_url = models.URLField(blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    director = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class WatchedMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    watched_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/10"
from django.db import models

# Create your models here.
