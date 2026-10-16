from django.shortcuts import render, redirect
from polls.forms import BlogForm
from polls.models import BlogPost
from polls.serializers import BlogPostSerializer

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )


def index(request):
    context = {
        "my_user": {
                    "is_authenticated": True,
                    "username": "SuperHero!"
                },
        "title": "Головна сторінка",
        "message": "Ласкаво просимо до POOLS/Django!",
        "copyright": "(c) django course 2026 (c) "
    }
    return render(request, "home.html", context)


def blogpost(request, post_id=0):
    if post_id:
        post = BlogPost.objects.get(id=post_id)

        if not post:
            raise IndexError(f"Record {post_id} not found")

        if request.method == "POST":
            form = BlogForm(request.POST)

            if form.is_valid():
                post.title = form.cleaned_data["title"]
                post.content = form.cleaned_data["content"]
                post.save()

                return redirect("blog")

        else:
            form = BlogForm(initial={
                "title": post.title,
                "content": post.content,
                "user": request.user
            })
    else:
        form = BlogForm(request.POST)
        if request.method == "POST" and form.is_valid():
            BlogPost.objects.create(
                    title=form.cleaned_data["title"],
                    content=form.cleaned_data["content"]
                )

            return redirect("blog")

        else:
            form = BlogForm()

    return render(
        request,
        "blogpost.html",
        {"form": form}
    )

# class PostListCreate(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
