from django.urls import path
from . import views


urlpatterns = [
    path("", views.CategoryView.as_view()),
    path("single/<int:category_id>", views.SingleCategory.as_view()),
    path("single/<int:category_id>/songs", views.SingleCategorySongView.as_view()),
    path("random", views.SingleRandomCategory.as_view())
]
