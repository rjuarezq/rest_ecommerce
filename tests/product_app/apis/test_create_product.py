from django.urls import reverse

from product_app.api.serializers import ProductSerializer
from product_app.models import Product
from tests.product_app.factories.product import ProductFactory
from tests.user_profile.utils import BasePerfilAPITestCase, login_profile


class ProductCreateApiTestCase(BasePerfilAPITestCase):
    @login_profile
    def test_create_product(self):
        self.product = ProductFactory.build()
        data = ProductSerializer(self.product).data
        resp = self.client.post(reverse("product_app:create-product"), data, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)
