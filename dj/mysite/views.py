
from django.shortcuts import render

from django.http import HttpResponse

def post_detail(request, post_id):
    context = {
        "title": "НЕ Головна сторінка",
        "message": f"200 > {post_id}",
        "request_data": f"{request.method}, {request.headers}",
        "copyright": "(c) django course 2026 "
    }
    return render(request, "home.html", context)
