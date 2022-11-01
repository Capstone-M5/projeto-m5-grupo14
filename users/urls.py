from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from users import views

urlpatterns = [
    path("login/", ObtainAuthToken.as_view()),
]
