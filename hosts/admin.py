from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.Host)
class CustomHostAdmin(admin.ModelAdmin):
    fieldsets = (("Custom Profile", {"fields": ("phone_number", "is_auth")},),)

    list_display = ("pk", "email", "username", "is_active", "is_staff", "is_auth")

