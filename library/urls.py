from django.urls import path
from . import views


urlpatterns = [
    path("", views.LibraryView.as_view()),
    path("<int:lib_id>", views.LibrarySingleView.as_view()),
    path("create", views.LibraryCreateView.as_view()),
    path("song", views.LibrarySongView.as_view()),
    path("song/<int:lib_id>", views.LibrarySongView.as_view()),
    path("create/lib-song", views.LibraryCreateAndAddSongView.as_view()),
    path("search/<str:search_query>", views.SearchLibraryView.as_view())
]
