from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("phone_number",)},),
    )

    list_filter = UserAdmin.list_filter + ("is_staff",)

    list_display = ("pk", "email", "username", "is_active", "is_staff", "is_superuser")
