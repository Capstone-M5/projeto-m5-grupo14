from django.urls import path
from reviews import views


urlpatterns = [
    path("video/<pk>/review/", views.ListCreateReview.as_view()), 
    path("video/review/<pk>/", views.RetrieveUpdateDestroyReviewView.as_view()), 

]
