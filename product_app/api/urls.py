from django.urls import path

from product_app.api.views import ProductCreateAPIView, ProductListAPIView

app_name = "product_app"
urlpatterns = [
    path("create/", ProductCreateAPIView.as_view(), name="create-product"),
    path("list/", ProductListAPIView.as_view(), name="list-product"),
]
