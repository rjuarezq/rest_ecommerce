from django import forms
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from user_profile.models import UserProfile


class UserProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            "password": forms.PasswordInput(render_value="*"),
        }
        fields = "__all__"

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserProfileChangeForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            "password": forms.PasswordInput(render_value="*"),
        }


@register(UserProfile)
class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm

    list_display = ["username", "email", "first_name", "last_name"]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    fieldsets = (
        (
            _("Personal info"),
            {"fields": ("username", "password", "email", "first_name", "last_name")},
        ),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )

    add_fieldsets = (
        (
            _("Personal Info"),
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get("password")
        if password:
            obj.set_password(password)
        return super().save_model(request, obj, form, change)
