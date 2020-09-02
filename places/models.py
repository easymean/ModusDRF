from django.db import models

from common import models as common_models


class Place(common_models.Common):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    description = models.TextField()
    policy = models.TextField()
    check_in = models.TimeField(default="00:00:00")
    check_out = models.TimeField(default="00:00:00")
    instant_book = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    max_guests = models.IntegerField(default=1)
    host = models.ForeignKey(
        "hosts.Host", on_delete=models.CASCADE, related_name="places"
    )
    location_code = models.CharField(max_length=10)

    def __str__(self):
        return f"pk:{self.pk}  name:{self.name}"

    def get_total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rate
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def get_first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    class Meta:
        ordering = ["-pk"]


class PlacePhoto(common_models.Common):
    file = models.ImageField()
    post = models.ForeignKey(
        "places.Place", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.post.name
