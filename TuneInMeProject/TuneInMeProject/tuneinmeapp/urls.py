from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('watched-movies/', views.watched_movies, name='watched_movies'),
    path('profile/', views.profile, name='profile'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
