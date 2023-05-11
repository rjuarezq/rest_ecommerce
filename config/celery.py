import os

from celery import Celery

app = Celery("proj")

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
app.config_from_object("django.conf:settings", namespace="CELERY")
