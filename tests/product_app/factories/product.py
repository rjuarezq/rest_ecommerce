from factory import Faker
from factory.django import DjangoModelFactory

from product_app.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker("name")
    description = Faker("text")
    price = Faker("pydecimal", left_digits=8, right_digits=2, positive=True)
    quantity = Faker("random_int")
