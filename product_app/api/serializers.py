from rest_framework.serializers import ModelSerializer

from product_app.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["uuid", "name", "price", "description", "quantity"]
