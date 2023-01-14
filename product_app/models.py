from django.db.models import CharField, DecimalField, Index, IntegerField, TextField
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel

PREFIX = "TB_"


class Product(TimeStampedModel):
    class Meta:
        db_table = PREFIX + "PRODUCTS"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        indexes = [Index(fields=["name"])]

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    name = CharField(verbose_name="Nombre", max_length=200, blank=False)
    description = TextField(verbose_name="Descripcion", default="", blank=True)
    price = DecimalField(verbose_name="Precio", max_digits=10, decimal_places=2, default=0.00)
    quantity = IntegerField(verbose_name="Cantidad", blank=False, null=False)


class CategoryProduct(TimeStampedModel):
    class Meta:
        db_table = PREFIX + "CATEGORY_PRODUCTS"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    name = CharField(verbose_name="Nombre", max_length=200, blank=False)
