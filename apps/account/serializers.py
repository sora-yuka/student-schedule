from typing import Dict
from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "username", 
            "email", 
            "password",
            ]

    def create(self, validated_data: Dict[str, str]) -> User:
        user = User.objects.create_user(**validated_data)
        # profile = Profile.objects.create()
        return user