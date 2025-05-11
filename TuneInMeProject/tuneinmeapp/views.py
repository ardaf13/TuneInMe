from django.shortcuts import render, redirect
from .models import WatchedMovie
from .forms import WatchedMovieForm

def home(request):
    return render(request, 'home.html')

def watched_movies(request):
    movies = WatchedMovie.objects.all()
    if request.method == 'POST':
        form = WatchedMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('watched_movies')
    else:
        form = WatchedMovieForm()
    return render(request, 'watched_movies.html', {'movies': movies, 'form': form})

def profile(request):
    total_movies = WatchedMovie.objects.count()
    points = total_movies * 10
    return render(request, 'profile.html', {'total_movies': total_movies, 'points': points})

def chatbot(request):
    recommendation = "Bugün sana Inception öneriyorum!"
    return render(request, 'chatbot.html', {'recommendation': recommendation})
