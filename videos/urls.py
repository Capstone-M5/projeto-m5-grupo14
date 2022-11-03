from django.urls import path
from . import views

urlpatterns = [
    path("video/", views.CreateVideoView.as_view()),
    path("videos/", views.ListTopVideosView.as_view()),
]
