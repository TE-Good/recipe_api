from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    # Orders the users by id.
    ordering = ["id"]
    # Displays the email and names in the list within admin.
    list_display = ["email", "name"]
    # Define the sections for the fieldsets within our change and create page.
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")}
        ),
        (_("Important Dates"), {"fields": ("last_login",)}),
    )
    # Defines the fields that will be displayed on the create user page.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2")
        }),
    )


# Creates the site where this is shown.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
