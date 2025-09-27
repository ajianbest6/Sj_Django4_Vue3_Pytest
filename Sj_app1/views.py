# views.py 用来接受用户的请求，并生成 HTTP 响应
from django.shortcuts import render
from django.http.response import HttpResponse
import os
from django.conf import settings


def submit(request):
    file_path = os.path.join(settings.BASE_DIR, 'resource', 'html', 'submit.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)


def result(request):
    html = 'I am result'
    return HttpResponse(html, status=404)
