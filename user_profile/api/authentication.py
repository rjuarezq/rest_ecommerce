from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class ExpireTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        self.token = self.get_model().objects.select_related("user").get(key=key)
        self.token = self.get_or_regenerate_token()
        return (self.token.user, self.token)

    def get_or_regenerate_token(self):
        if self.is_token_expired():
            return self.refresh_token()
        return self.token

    def is_token_expired(self) -> bool:
        return self.token_expires_in() < timedelta(seconds=0)

    def token_expires_in(self) -> timedelta:
        time_elapsed = timezone.now() - self.token.created
        time_left = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return time_left

    def refresh_token(self):
        user = self.token.user
        self.token.delete()
        token = self.get_model().objects.create(user=user)
        return token
