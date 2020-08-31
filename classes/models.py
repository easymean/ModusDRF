from django.db import models
from common import models as common_models


class Class(common_models.Common):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField(default="00:00:00")
    end_time = models.TimeField(default="00:00:00")
    is_finished = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    max_guests = models.IntegerField(default=1)
    policy = models.TextField()
    is_allowed = models.BooleanField(default=False)
    address = models.CharField(max_length=500)
    somm = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="classes", null=True
    )
    location_code = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pk"]


class ClassPhoto(common_models.Common):
    file = models.ImageField()
    post = models.ForeignKey(
        "classes.Class", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.post.title
