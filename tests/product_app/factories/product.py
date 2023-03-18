from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from product_app.models import CategoryProduct, Product


class CategoryProductFactory(DjangoModelFactory):
    class Meta:
        model = CategoryProduct
        django_get_or_create = ["name"]

    name = Faker("name")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker("name")
    description = Faker("text")
    price = Faker("pydecimal", left_digits=8, right_digits=2, positive=True)
    quantity = Faker("random_int")
    category = SubFactory(CategoryProductFactory)
