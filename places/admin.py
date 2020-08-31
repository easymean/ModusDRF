from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):
    model = models.PlacePhoto


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "price", "max_guests",)},),
        ("Status", {"fields": ("instant_book", "is_active")}),
        ("Times", {"fields": ("check_in", "check_out")}),
        ("Address", {"fields": ("address",)}),
        ("Policy", {"fields": ("policy",)}),
        ("Manager", {"fields": ("host",)}),
    )

    list_display = ("pk", "name", "price", "max_guests", "is_active")


@admin.register(models.PlacePhoto)
class PlacePhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"

