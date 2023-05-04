from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpireTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().Objects.select_related("user").get(key=self.token)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed(_("Invalid token."))
        if not token.user.is_active:
            raise AuthenticationFailed(_("User inactive or deleted."))
        if self.token_expired_handler(token):
            raise AuthenticationFailed(_("The Token is expired."))
        return (token.user, token)

    def token_expired_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            ...
        return is_expired

    def is_token_expired(self, token) -> bool:
        return self.token_expires_in(token) < timedelta(seconds=0)

    def token_expires_in(self, token) -> timedelta:
        time_elapsed = timezone.now() - token.created
        time_left = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return time_left
