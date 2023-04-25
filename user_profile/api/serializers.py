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

    def create(self, validated_data):
        validated_data["password"] = PasswordHasher().hash(validated_data["password"])
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)
        instance.password = PasswordHasher().hash(instance.password)
        instance.save()
        return instance


class UserTokenSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "email", "first_name", "last_name"]
