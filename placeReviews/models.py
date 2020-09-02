from django.db import models
from common.models import Common
from django.core.validators import MinValueValidator, MaxValueValidator


class PlaceReview(Common):
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    place = models.ForeignKey(
        "places.Place", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.place} - {self.pk} by {self.user}"
