import os

from celery import Celery
from django.conf import settings
from kombu import Queue

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("config", broker=settings.CELERY_BROKER_URL)

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

# Consider if you have some problems with the configurations
# https://forum.djangoproject.com/t/celery-does-not-register-tasks/14560/7
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
