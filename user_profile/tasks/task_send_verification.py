from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context

from config.celery_app import app
from core.utils.email import Email
from user_profile.models import UserProfile


@receiver(post_save, sender=UserProfile)
@app.task(blind=True)
def task_email_verification(sender, instance, created, *args, **kwargs):
    print("hello send email")
    if created:
        user = instance
        email = Email(
            to=user.email,
            subject="Bienvenido a la plataforma",
            sender=settings.SMTP_USERNAME,
        )
        email.set_template_with_context(
            "email/confirm_register.html", context={"username": user.first_name}
        )
        email.send()
