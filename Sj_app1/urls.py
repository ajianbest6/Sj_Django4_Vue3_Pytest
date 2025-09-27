from django.urls import path
from .views import submit, result


urlpatterns = [
    path("submit/", submit),
    path("result/", result),
]