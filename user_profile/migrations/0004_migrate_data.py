from django.db import migrations


def forwards_encrypted_char(apps, schema_editor):
    UserProfile = apps.get_model("user_profile", "UserProfile")

    for row in UserProfile.objects.all():
        row.password = row.old_password
        row.save(update_fields=["password"])


def reverse_encrypted_char(apps, schema_editor):
    UserProfile = apps.get_model("user_profile", "UserProfile")

    for row in UserProfile.objects.all():
        row.old_password = row.password
        row.save(update_fields=["old_password"])


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0003_add_encrypted_password"),
    ]

    operations = [
        migrations.RunPython(forwards_encrypted_char, reverse_encrypted_char),
    ]
