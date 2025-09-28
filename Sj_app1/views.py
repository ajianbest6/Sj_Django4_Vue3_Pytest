# views.py 用来接受用户的请求，并生成 HTTP 响应
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
import os
from django.conf import settings
from .models import FeedBack


def submit(request):
    if request.method == 'POST':
        data = {
            'quality': int(request.POST['quality']),
            'attitude': int(request.POST['service']),
            'speed': int(request.POST['delivery']),
            'comment': request.POST['comment'],
            'anonymous': request.POST['anonymous'] == 'true',
        }

        # obj = FeedBack(**data)
        # obj.save()

        FeedBack.objects.create(**data)
    
        return HttpResponseRedirect('http://127.0.0.1:8000/feedback/result/')
    
    file_path = os.path.join(settings.BASE_DIR, 'resource', 'feedback', 'submit.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)


def result(request):
    file_path = os.path.join(settings.BASE_DIR, 'resource', 'feedback', 'result.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)
