# Generated by Django 4.1.2 on 2022-11-05 18:14

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("text", models.TextField(max_length=400)),
                (
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
