from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# register serializer
class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])

        user_profile = UserProfile.objects.create(
            user=user,
            role=validated_data['role'],
            )
        user_profile.save()
        return user


# user serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
