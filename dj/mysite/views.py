
from django.shortcuts import render

from django.http import HttpResponse
from polls.models import BlogPost, Tags, Article


def post_detail(request, post_id):
    context = {
        "my_user": {
            "is_authenticated": True,
            "username": "anon"
        },
        "title": "MYSITE > Головна сторінка",
        "message": f"200 > {post_id}",
        "request_data": f"{request.method}, {request.headers}",
        "copyright": "(c) django course 2026 "
    }
    return render(request, "home.html", context)


def blog_list(request):
    # 1. Отримуємо дані
    posts = BlogPost.objects.all().order_by("-created_at")
    
    # 2. Готуємо контекст
    context = {
        "title": "Мій блог",
        "posts": posts,
        "author": "Олександр"
    }
    
    # 3. Передаємо у шаблон
    return render(request, "blog.html", context)


def blog_create(request, post_id):
    blogpost = BlogPost.objects.create(
        title=f"Title #{post_id} ",
        content="Lorem ipsum ljkfuifh jkefjiui k",

    )
    return render(request, "blog.html", {"post": blogpost})