from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created_at']

    def update(self, instance, validated_data):
        instance.text = validated_data.get("text", instance.text)
        instance.rating = validated_data.get(
            "rating", instance.rating)

        instance.save()

        return instance
