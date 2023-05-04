from django.contrib.admin import ModelAdmin, register

from product_app.models import CategoryProduct, Product

# Register your models here.


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("name", "price", "quantity")


@register(CategoryProduct)
class CategoryProductAdmin(ModelAdmin):
    list_display = ["name"]
