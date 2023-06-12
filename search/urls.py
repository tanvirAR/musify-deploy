from django.urls import path
from . import views

urlpatterns = [
    path("<str:query>", views.SearchView.as_view()),
    # path("", views.Search.as_view())
]
