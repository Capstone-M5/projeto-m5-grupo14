from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    text = models.TextField(max_length=400)
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ],
    )
    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    video = models.ForeignKey(
        "videos.Video", on_delete=models.CASCADE, related_name="reviews"
    )
