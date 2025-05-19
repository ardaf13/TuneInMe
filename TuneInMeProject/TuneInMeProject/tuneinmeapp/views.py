from django.shortcuts import render, redirect
from .models import WatchedMovie, UserProfile
from .forms import WatchedMovieForm
from datetime import date, timedelta

def home(request):
    return render(request, 'home.html')


def watched_movies(request):
    demo_user_id = 1  # Simulated user for demo
    movies = WatchedMovie.objects.all()

    if request.method == 'POST':
        form = WatchedMovieForm(request.POST)
        if form.is_valid():
            watched_movie = form.save(commit=False)
            watched_movie.user_id = demo_user_id
            watched_movie.save()

            return redirect('watched_movies')
    else:
        form = WatchedMovieForm()

    return render(request, 'watched_movies.html', {'movies': movies, 'form': form})


def profile(request):
    demo_user_id = 1  # Demo user ID
    profile, _ = UserProfile.objects.get_or_create(user_id=demo_user_id)
    watched_movies = WatchedMovie.objects.filter(user_id=demo_user_id)

    # Update points based on total watched movies
    total_watched = watched_movies.count()
    profile.points = total_watched * 10

    # Update level based on watched movie count
    if total_watched < 1:
        profile.level = "Ruh Halinin Magellanı"
    elif total_watched < 3:
        profile.level = "Duygusal Kaşif"
    elif total_watched < 5:
        profile.level = "Sinema Ustası"
    else:
        profile.level = "Film Gurusu"

    # Handle streak
    if profile.last_watched_date != date.today():
        if profile.last_watched_date == date.today() - timedelta(days=1):
            profile.streak_count += 1
        else:
            profile.streak_count = 0
        profile.last_watched_date = date.today()

    # Handle weekly challenges (reset every Monday)
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    if profile.last_challenge_reset is None or profile.last_challenge_reset < start_of_week:
        profile.weekly_challenges = [
            "1 yabancı dilde film izle",
            "2 farklı türde film izle",
            "3 gün üst üste film izle"
        ]
        profile.last_challenge_reset = today

    profile.save()

    context = {
        'total_movies': total_watched,
        'points': profile.points,
        'level': profile.level,
        'streak_count': profile.streak_count,
        'weekly_challenges': profile.weekly_challenges,
    }
    return render(request, 'profile.html', context)


def chatbot(request):
    recommendation = "Bugün sana Inception öneriyorum!"
    return render(request, 'chatbot.html', {'recommendation': recommendation})
