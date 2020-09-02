from datetime import date
from django.db import models

from common.models import Common


class PlaceReservation(Common):

    is_allowed = models.CharField(max_length=5)
    payment_type = models.CharField(max_length=5)
    date = models.DateField(blank=False, null=False, default=date.today)
    check_in = models.TimeField(blank=False, null=False, default="00:00:00")
    check_out = models.TimeField(blank=False, null=False, default="00:00:00")
    guests_num = models.IntegerField(blank=False, null=False, default=1)
    place = models.ForeignKey(
        "places.Place", on_delete=models.CASCADE, related_name="reservations"
    )
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="place_reservations"
    )

    def __str__(self):
        return f"{self.pk} {self.date}"

    class Meta:
        ordering = ["-pk"]

