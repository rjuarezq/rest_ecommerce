from django.urls import reverse
from rest_framework import status

from tests.user_profile.factories.user import UserFactory
from tests.user_profile.utils import BasePerfilAPITestCase, login_profile
from user_profile.api.serializers import UserCreateSerializer
from user_profile.models import UserProfile


class UserCreateAPIViewTestCase(BasePerfilAPITestCase):
    # @activate
    @login_profile
    def test_create_account(self):
        self.acc = UserFactory.build()

        url = reverse("user_profile:create-user")
        data = UserCreateSerializer(self.acc).data
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)
