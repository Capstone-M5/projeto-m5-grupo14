from rest_framework import serializers
from .models import User


class UserSerializeer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}
        ...

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        ...

    ...
