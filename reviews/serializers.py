from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Review
from videos.models import Video

class VideoListDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video

        exclude = ["users"]


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    video = VideoListDetailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created_at', 'users', 'video']

    def update(self, instance, validated_data):
        instance.text = validated_data.get("text", instance.text)
        instance.rating = validated_data.get(
            "rating", instance.rating)

        instance.save()

        return instance



