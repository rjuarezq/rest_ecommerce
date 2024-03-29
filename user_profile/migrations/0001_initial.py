# Generated by Django 3.2 on 2023-04-12 01:52

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo')),
                ('password', models.CharField(max_length=512, verbose_name='Contraseña')),
                ('date_of_birth', models.DateField(blank=True, default='2000-01-01', max_length=10, null=True, verbose_name='Fecha de nacimiento')),
                ('image_profile', models.ImageField(blank=True, null=True, upload_to='user_profile/', verbose_name='Imagen de perfil')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Administrador')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super Usuario')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'TB_USER_PROFILE',
            },
        ),
    ]
