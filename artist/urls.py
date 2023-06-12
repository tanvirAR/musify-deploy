from django.urls import path
from . import views


urlpatterns = [
    path("<int:artist_id>", views.ArtistView.as_view()),
    path("random/<int:number>", views.RandomArtistsView.as_view()),
    path("<int:artist_id>/song", views.ArtistSongView.as_view()),
    path("multiples/", views.MultipleArtistsView.as_view())
]


