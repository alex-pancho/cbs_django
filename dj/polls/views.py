from django.shortcuts import render

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


def how(request):
    return HttpResponse("Hello! How are you?")
