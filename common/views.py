from rest_framework.permissions import IsAuthenticated


class AuthenticatedView:
    permission_classes = [IsAuthenticated]
