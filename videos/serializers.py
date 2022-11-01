from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ["downloads", "users"]
        ...

    def create(self, validated_data):
        movie = Video.objects.get_or_create(**validated_data)
        movie.downloads = movie.downloads + 1
        return movie
        ...
    ...
