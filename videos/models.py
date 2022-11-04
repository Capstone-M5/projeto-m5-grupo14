from django.db import models
import uuid
from users.models import User


class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=128)
    thumbnail = models.TextField()
    link = models.CharField(max_length=128, unique=True)
    downloads = models.PositiveIntegerField(default=0)
    users = models.ManyToManyField(
        "users.User", through="Downloaded", related_name="videos", blank=True)


class Downloaded(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
