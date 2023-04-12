from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView

from common.views import AuthenticatedView
from user_profile.api.serializers import UserCreateSerializer, UserSerializer
from user_profile.models import UserProfile


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserListAPIView(AuthenticatedView, ListAPIView):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.filter(is_active=True)


class UserRetrieveUpdateAPIView(AuthenticatedView, RetrieveUpdateAPIView):
    serializer_class = UserCreateSerializer
    queryset = UserProfile.objects.filter(is_active=True)
