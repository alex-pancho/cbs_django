from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {
        "title": "Головна сторінка",
        "message": "Ласкаво просимо до Django!",
    }
    return render(request, "home.html", context)


def how(request):
    return HttpResponse("Hello! How are you?")
