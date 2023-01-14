from argon2 import PasswordHasher
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django_cryptography.fields import encrypt
from model_utils.fields import UUIDField


class UserProfile(AbstractUser):
    class Meta:
        db_table = "TB_USER_PROFILE"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    password = encrypt(CharField(verbose_name="Contraseña", max_length=15))
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def save(self, *args, **kwargs):
        ph = PasswordHasher()
        self.password = ph.hash(self.password)
        return super().save(*args, **kwargs)
