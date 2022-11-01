import ipdb

from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class AccountsViews(generics.CreateAPIView):
    queryset = User.objects.all()
    get_serializer = UserSerializer

# Create your views here.
