from django.urls import path
from . import views


urlpatterns = [
    path("<int:song_id>", views.SongView.as_view()),
    path("random/<int:number_of_songs>", views.RandomSongs.as_view()),
    path("multiples/", views.MultipleSongsView.as_view())
]
