from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from users import views

urlpatterns = [
    path("register/", views.AccountsViews.as_view()),
    path("login/", ObtainAuthToken.as_view()),
    path("profile/me/", views.AccountsDetailsViews.as_view()),
    path("profile/", views.UsersViews.as_view()),
]
