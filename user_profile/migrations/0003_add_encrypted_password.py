from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_rename_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="password",
            field=django_cryptography.fields.encrypt(
                models.CharField(blank=True, null=True, max_length=15)
            ),
            preserve_default=False,
        ),
    ]
