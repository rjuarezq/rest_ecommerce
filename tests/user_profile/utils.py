from functools import wraps

from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate

from tests.user_profile.factories.user import UserFactory


class BasePerfilAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.add_perfil()
        cls.add_initial()
        super().setUpTestData()

    @classmethod
    def add_perfil(cls):
        cls.perfil = UserFactory.create()

    @classmethod
    def add_initial(cls):
        return


class BasePerfilTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.add_perfil()

    @classmethod
    def add_perfil(cls):
        cls.acc = UserFactory.create()


def login_profile(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.client.force_authenticate(user=self.perfil)
        return func(self, *args, **kwargs)

    return wrapper
