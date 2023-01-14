from rest_framework.generics import CreateAPIView, ListAPIView

from common.views import AuthenticatedView
from product_app.api.serializers import ProductSerializer
from product_app.models import Product


# Create your views here.
class ProductCreateAPIView(AuthenticatedView, CreateAPIView):
    serializer_class = ProductSerializer


class ProductListAPIView(AuthenticatedView, ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
