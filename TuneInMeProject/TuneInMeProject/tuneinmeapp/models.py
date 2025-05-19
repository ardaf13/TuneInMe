from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class WatchedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} watched {self.movie.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    taste_profile = models.JSONField(default=dict, blank=True)
    points = models.IntegerField(default=0)
    level = models.CharField(max_length=100, default="Başlangıç")
    streak_count = models.IntegerField(default=0)
    last_watched_date = models.DateField(null=True, blank=True)
    last_challenge_reset = models.DateField(null=True, blank=True)
    weekly_challenges = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.user.username
