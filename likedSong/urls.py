from django.urls import path
from . import views

urlpatterns = [
    path("", views.LikedSongView.as_view()),
    path("remove", views.SingleLikedSongViewClass.as_view()),
    path("check/<int:trackId>", views.SingleLikedSongViewClass.as_view())
]
