from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0004_migrate_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="old_password",
        ),
    ]
