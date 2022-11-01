from rest_framework import serializers
from reviews.models import Review

from videos.serializers import VideoSerializer
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}
        ...

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        ...

    ...


class UserReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ["users"]


class UserRetriveUpdateSerializer(serializers.ModelSerializer):

    videos = VideoSerializer(many=True, read_only=True)
    reviews = UserReviewListSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "name",
            "email", 
            "videos",
            "reviews"
        ]




