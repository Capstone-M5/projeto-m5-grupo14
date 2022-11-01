from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("thumbnail", models.CharField(max_length=128)),
                ("link", models.CharField(max_length=128, unique=True)),
                ("downloads", models.PositiveIntegerField(default=0)),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="videos", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
