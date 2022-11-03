from django.urls import path
from reviews import views


urlpatterns = [
    path("video/review/<pk>/", views.RetrieveUpdateDestroyReviewView.as_view()), ]
