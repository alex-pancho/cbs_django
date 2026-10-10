from django.urls import include, path
from django.contrib.auth.views import LoginView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from . import views
from .api_models import PostList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')

urlpatterns = [
    path("", views.index, name="index"),
    # path("index", views.index, name="index"),
    path("blogpost/", views.blogpost, name="blogpost"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(),name="login"),
    path("login/blogpost/", views.blogpost, name="blogpost"),
    # path("api/posts/", PostList.as_view()),
    # path('api/posts/', views.post_list, name='api-post-list'),
    # path('api/posts/<int:pk>/', views.post_detail, name='api-post-detail'),
    # path('api/posts/', views.PostListCreate.as_view(), name='api-post-list'),
    # path('api/posts/<int:pk>/', views.PostDetail.as_view(), name='api-post-detail'),
    path('api/', include(router.urls)),
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