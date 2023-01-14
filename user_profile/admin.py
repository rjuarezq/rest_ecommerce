from django.contrib.admin import ModelAdmin, register

from user_profile.models import UserProfile


@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ("username", "email", "is_superuser", "is_active")
