from rest_framework.authentication import BasicAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from .authentication import ExpireTokenAuthentication


class Authentication:
    def get_data_user(self, request):
        try:
            _, token = get_authorization_header(request).split()
        except ValueError:
            raise AuthenticationFailed
        token_manager = ExpireTokenAuthentication()
        token_manager.authenticate_credentials(token.decode())
        print(token)

    def dispatch(self, request, *args, **kwargs):
        self.get_data_user(request)
        return super().dispatch(request, *args, **kwargs)
