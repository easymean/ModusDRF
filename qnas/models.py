from django.db import models
from common.models import Common


class PlaceQuestion(Common):
    question = models.TextField()
    place = models.ForeignKey(
        "places.Place", on_delete=models.CASCADE, related_name="questions"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="place_questions"
    )

    def __str__(self):
        return self.pk


class PlaceReply(Common):
    reply = models.TextField()
    question = models.ForeignKey(
        "qnas.PlaceQuestion", on_delete=models.CASCADE, related_name="replies"
    )
    host = models.ForeignKey(
        "hosts.Host", on_delete=models.CASCADE, related_name="replies"
    )

    def __str__(self):
        return self.pk
