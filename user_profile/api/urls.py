from django import urls
from django.urls import include, path
from magic_link import urls as magic_link_urls

from user_profile.api.views import (
    Login,
    Logout,
    TokenRetrieveAPIView,
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveUpdateAPIView,
)

app_name = "user_profile"
urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="create-user"),
    path("list/", UserListAPIView.as_view(), name="list-user"),
    path("update/<uuid:pk>/", UserRetrieveUpdateAPIView.as_view(), name="edit-user"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("refresh-token/", TokenRetrieveAPIView.as_view(), name="refresh-token"),
    path("magic_link/", include(magic_link_urls)),
]
