from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    # video = VideoSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created_at']


        
        
