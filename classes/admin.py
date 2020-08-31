from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):
    model = models.ClassPhoto


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Info", {"fields": ("title", "description", "price", "max_guests",)},),
        ("Status", {"fields": ("is_finished", "is_allowed", "is_active")}),
        ("Times", {"fields": ("start_time", "end_time")}),
        ("Address", {"fields": ("address",)}),
        ("Policy", {"fields": ("policy",)}),
        ("Manager", {"fields": ("somm",)}),
    )

    list_display = (
        "pk",
        "title",
        "price",
        "is_finished",
        "is_active",
        "max_guests",
    )


@admin.register(models.ClassPhoto)
class ClassPhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"

