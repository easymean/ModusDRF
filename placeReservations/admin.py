from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.PlaceReservation)
class PlaceReservationAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Status", {"fields": ("payment_type", "is_allowed", "is_active")}),
        ("Times", {"fields": ("date", "check_in", "check_out")}),
        ("Guest", {"fields": ("guest", "guests_num")}),
        ("Place", {"fields": ["place"]}),
    )

    list_display = ("pk", "is_allowed", "place", "guest", "is_active")

