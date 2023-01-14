from factory import Faker
from factory.django import DjangoModelFactory

from user_profile.models import UserProfile


class UserFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile
        django_get_or_create = ["username"]

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    username = Faker("user_name")
    password = Faker("user_name")
