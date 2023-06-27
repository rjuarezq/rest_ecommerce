from django.contrib.auth.hashers import make_password
from rest_framework.serializers import CharField, ModelSerializer, Serializer

from user_profile.models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["uuid", "username", "password", "email", "first_name", "last_name"]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "username", "password"]
        extra_kwargs = {"password": {"style": {"input_type": "password"}}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password, hasher="argon2")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)
        instance.password = make_password(instance.password, hasher="argon2")
        instance.save()
        return instance


class UserTokenSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "email", "first_name", "last_name"]


class UserVerificationSerializer(Serializer):
    key = CharField(read_only=True, max_length=40)
