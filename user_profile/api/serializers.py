from argon2 import PasswordHasher
from django.core.signing import Signer
from rest_framework.serializers import CharField, EmailField, ModelSerializer

from user_profile.models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["uuid", "username", "password", "email", "first_name", "last_name"]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "username", "password"]

    password = CharField(style={"input_type": "password"})
    email = EmailField(required=True)
