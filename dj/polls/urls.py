from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("index", views.index, name="index"),
    path("blogpost/", views.blogpost, name="blogpost"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(),name="login"),
    path("login/blogpost/", views.blogpost, name="blogpost"),
]