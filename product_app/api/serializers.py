from rest_framework.serializers import ModelSerializer

from product_app.models import CategoryProduct, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["uuid", "name", "price", "description", "quantity", "category"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = ["uuid", "name"]
