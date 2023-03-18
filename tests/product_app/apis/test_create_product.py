from django.urls import reverse

from product_app.api.serializers import ProductSerializer
from product_app.models import CategoryProduct, Product
from tests.product_app.factories.product import CategoryProductFactory, ProductFactory
from tests.user_profile.utils import BasePerfilAPITestCase, login_profile


class ProductCreateApiTestCase(BasePerfilAPITestCase):
    @login_profile
    def test_create_product(self):
        self.cp = CategoryProductFactory.create()
        self.product = ProductFactory.build(category=self.cp)
        serializer = ProductSerializer(self.product, data=self.product.__dict__)
        serializer.is_valid(raise_exception=True)
        resp = self.client.post(
            reverse("product_app:create-product"), serializer.data, format="json"
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)
