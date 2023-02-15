# Stdlib Imports
import random
from typing import OrderedDict

# Django Imports
from django.db import transaction
from django.db.models import Q
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Rest Framework Imports
from rest_framework import serializers, exceptions

# Third Party Imports
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.state import token_backend


# Own Imports
from authy.models import  User, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "email",
            "phone_number",
            "date_created",
            "date_modified",
            "password",
        ]
        extra_kwargs = {
            "address": {"read_only": True},
            "is_active": {"read_only": True},
        }
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password')
        return representation

    def validate_password(self, value):
        return make_password(value)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('student_number', )
        

class UserLoginObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer to authenticate the user email and password."""

    username_field = "email"

    def validate(self, data):

        password = data.get("password")
        email = data.get("email")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed({"message": "Wrong username or password"})

        if user.check_password(password):
            refresh = self.get_token(user)
            serializer = UserSerializer(user)
            payload = {
                "status": 200,
                "success": True,
                "message": "Login successful.",
                "data": serializer.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
            return payload

        raise exceptions.AuthenticationFailed({"message": "Wrong username or password"})


class UserTokenRefreshSerializer(TokenRefreshSerializer):
    """Serializer to decode and update access token."""

    def validate(self, attrs):
        data = super(UserTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data["access"], verify=True)

        """Get and serialzier user object"""
        user = User.objects.get(id=decoded_payload["user_id"])
        serializer = UserSerializer(user)

        payload = {"access": data["access"], "data": serializer.data}
        return payload
