from django.db.models import (
    PROTECT,
    CharField,
    DecimalField,
    ForeignKey,
    Index,
    IntegerField,
    TextField,
)
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel

PREFIX = "TB_"


class CategoryProduct(TimeStampedModel):
    class Meta:
        db_table = PREFIX + "CATEGORY_PRODUCTS"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    name = CharField(verbose_name="Nombre", max_length=200, blank=False)

    def __str__(self) -> str:
        return f"{self.name} | {self.uuid}"


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
    category = ForeignKey(
        CategoryProduct,
        on_delete=PROTECT,
        blank=False,
        null=False,
        verbose_name="Categoria",
        default="4e5d2e47-9e7b-4c5f-b673-20724866c74b",
    )
