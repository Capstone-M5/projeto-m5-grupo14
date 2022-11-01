
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=128)
    ...
