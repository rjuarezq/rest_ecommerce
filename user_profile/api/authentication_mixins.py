from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import NotAuthenticated

from .authentication import ExpireTokenAuthentication


class Authentication:
    def get_user(self, request):
        try:
            _, token = get_authorization_header(request).split()
        except ValueError:
            raise NotAuthenticated
        self.validate_token(token)

    def dispatch(self, request, *args, **kwargs):
        self.get_user(request)
        if self.user:
            return super().dispatch(request, *args, **kwargs)
        return JsonResponse(
            {"message": "User is not authenticated"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def validate_token(self, token):
        self.user = None
        token_manager = ExpireTokenAuthentication()
        token = token_manager.authenticate_credentials(token.decode())
        if not token:
            return
        self.user = token.user
