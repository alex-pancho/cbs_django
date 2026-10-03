from django.shortcuts import render, redirect
from polls.forms import BlogForm
from polls.models import BlogPost
from django.http import HttpResponse


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
                "content": post.content
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
