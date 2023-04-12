from django.urls import path

from user_profile.api.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveUpdateAPIView,
)

app_name = "user_profile"
urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="create-user"),
    path("list/", UserListAPIView.as_view(), name="list-user"),
    path("update/<uuid:pk>/", UserRetrieveUpdateAPIView.as_view(), name="edit-user"),
]
