from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http.request import HttpRequest
from magic_link.models import MagicLink

from config.celery_app import app
from core.utils.email import Email
from user_profile.models import UserProfile


# BUG: CELERY DON'T RECOGNIZE THIS TASK
@receiver(post_save, sender=UserProfile)
# @app.task(blind=True)
def task_email_verification(sender, instance, created, *args, **kwargs):
    if created:
        user = instance
        verification_link = generate_token_verification(user)
        email = Email(
            to=user.email,
            subject=f"Welcome- {user.username}",
            sender=settings.SMTP_USERNAME,
        )
        email.set_template_with_context(
            "email/confirm_register.html",
            context={"username": user.first_name, "link": verification_link},
        )
        email.send()


def generate_token_verification(user: UserProfile) -> str:
    link = MagicLink.objects.create(user=user, redirect_to="/")
    # TODO: fix this import the correct requestr
    url = HttpRequest.build_absolute_uri(link.get_absolute_url())
    return url
