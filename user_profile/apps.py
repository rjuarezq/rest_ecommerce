from importlib import import_module

from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_profile"

    def ready(self):
        import_module("user_profile.tasks.task_send_verification")
