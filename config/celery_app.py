import os

from celery import Celery
from django.conf import settings
from kombu import Queue

app = Celery("celery_app", broker=settings.CELERY_BROKER_URL)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# Collect variables with prefix CELERY_ from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.task_queues = {
    Queue("email"),
}

app.conf.task_routes = {
    "user_profile.*": {
        "queue": "email",
    },
}
