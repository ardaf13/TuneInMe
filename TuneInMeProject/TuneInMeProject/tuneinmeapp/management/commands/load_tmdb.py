import requests
from django.core.management.base import BaseCommand
from tuneinmeapp.models import Movie

API_KEY = '9634acfd4f9d41af469a2ea3dd6e71b3'

class Command(BaseCommand):
    help = 'Load popular movies from TMDb (up to 1000 movies)'

    def handle(self, *args, **kwargs):
        genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US'
        genre_response = requests.get(genre_url)
        genre_map = {g['id']: g['name'] for g in genre_response.json().get('genres', [])}

        for page in range(1, 51):  # 50 pages * 20 movies per page = 1000 movies
            url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}'
            response = requests.get(url)
            movies = response.json().get('results', [])

            if not movies:
                break  # Stop if no more movies are returned

            for movie in movies:
                title = movie.get('title')
                overview = movie.get('overview')
                release_date = movie.get('release_date')
                poster_url = f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get('poster_path') else ''
                genre_ids = movie.get('genre_ids', [])
                genre_names = ', '.join([genre_map.get(gid, 'Unknown') for gid in genre_ids])

                Movie.objects.get_or_create(
                    title=title,
                    description=overview,
                    release_year=int(release_date.split('-')[0]) if release_date else None,
                    poster_url=poster_url,
                    genre=genre_names
                )

            self.stdout.write(self.style.SUCCESS(f'Page {page} loaded successfully.'))

        self.stdout.write(self.style.SUCCESS('All available popular movies loaded successfully.'))
