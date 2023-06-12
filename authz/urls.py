from django.urls import path
from . import views


urlpatterns = [
    path("", views.LoginView.as_view()),
    path("signup", views.SignUpView.as_view()),
    path("auth-by-google", views.login_with_google)
]
