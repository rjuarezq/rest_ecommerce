from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    Permission,
)
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    EmailField,
    ImageField,
    ManyToManyField,
)
from django.utils import timezone
from model_utils.fields import UUIDField


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    class Meta:
        db_table = "TB_USER_PROFILE"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    username = CharField(verbose_name="Nombre de usuario", max_length=100, unique=True)
    first_name = CharField(verbose_name="Nombre(s)", max_length=100)
    last_name = CharField(verbose_name="Apellidos", max_length=100)
    email = EmailField(verbose_name="Correo", max_length=100, unique=True)
    password = CharField(verbose_name="Contraseña", max_length=512)
    date_of_birth = DateField(
        verbose_name="Fecha de nacimiento",
        max_length=10,
        blank=True,
        null=True,
        default="2000-01-01",
    )
    image_profile = ImageField(
        verbose_name="Imagen de perfil", upload_to="user_profile/", blank=True, null=True
    )
    is_active = BooleanField(verbose_name="Activo", default=True)
    is_staff = BooleanField(verbose_name="Administrador", default=False)
    is_superuser = BooleanField(verbose_name="Super Usuario", default=False)
    date_joined = DateTimeField(verbose_name="Fecha de registro", default=timezone.now)
    groups = ManyToManyField(Group, blank=True)
    user_permissions = ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="user_set",
        related_query_name="user",
    )
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return f"{self.username}-{self.email}-{self.first_name}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        return True

    def get_data_params(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
            "is_staff": self.is_staff,
            "is_superuser": self.is_superuser,
        }
