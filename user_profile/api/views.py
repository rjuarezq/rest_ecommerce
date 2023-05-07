from datetime import datetime

from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response

from common.views import AuthenticatedView
from user_profile.api.serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserTokenSerializer,
)
from user_profile.models import UserProfile

from .authentication_mixins import Authentication


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserListAPIView(Authentication, ListAPIView):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.filter(is_active=True)


class UserRetrieveUpdateAPIView(AuthenticatedView, RetrieveUpdateAPIView):
    serializer_class = UserCreateSerializer
    queryset = UserProfile.objects.filter(is_active=True)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        if not user.is_active:
            return Response(
                data={"message:": "User is not active"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserTokenSerializer(user)

        if not created:
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                _delete_current_sessions(all_sessions, user)
            token.delete()
            token = Token.objects.create(user=user)

        return Response(
            data={
                "token": token.key,
                "user": user_serializer.data,
                "message": "Token generated",
            },
            status=status.HTTP_201_CREATED,
        )


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        current_token = request.GET.get("Token")
        if not current_token:
            return Response(
                data={"message": "Token not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token = Token.objects.get(key=current_token)
        if token:
            user = token.user
            token.delete()
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                _delete_current_sessions(all_sessions, user)

        return Response(
            data={"message": "Token deleted"},
            status=status.HTTP_200_OK,
        )


class TokenRetrieveAPIView(Authentication, RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        token = Token.objects.select_related("user").get(user__username=self.user.username)
        return Response({"token": token.key})


def _delete_current_sessions(all_sessions: Session, user):
    for session in all_sessions:
        session_data = session.get_decoded()
        if str(user.pk) == session_data.get("_auth_user_id"):
            session.delete()
