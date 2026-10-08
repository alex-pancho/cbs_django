from django.urls import path
from django.contrib.auth.views import LoginView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from . import views
from .api_models import PostList

urlpatterns = [
    path("", views.index, name="index"),
    # path("index", views.index, name="index"),
    path("blogpost/", views.blogpost, name="blogpost"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(),name="login"),
    path("login/blogpost/", views.blogpost, name="blogpost"),
    path("api/posts/", PostList.as_view()),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
    ),
]