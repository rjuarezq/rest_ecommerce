from os import getenv

from celery import Celery

CELERY_USER = getenv("CELERY_USER", "guest")
CELERY_PASSWORD = getenv("CELERY_PASSWORD", "guest")
CELERY_HOST = getenv("CELERY_HOST", "localhost")
CELERY_PORT = getenv("CELERY_PORT", "5672")
CELERY_DATABASE = getenv("CELERY_DATABASE", "celery")

CELERY_BROKER_URL = (
    f"pyamqp://{CELERY_USER}:{CELERY_PASSWORD}@{CELERY_HOST}:{CELERY_PORT}/{CELERY_DATABASE}"
)

app = Celery("celery_app", broker=CELERY_BROKER_URL)

app.conf.task_queues = []
