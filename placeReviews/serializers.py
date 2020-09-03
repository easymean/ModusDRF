from rest_framework import serializers

from .models import PlaceReview

from users.serializers import RelationUserSerializer
from places.serializers import RelationPlaceSerializer


class ReviewSerializer(serializers.ModelSerializer):

    user = RelationUserSerializer(read_only=True)
    place = RelationPlaceSerializer(read_only=True)

    class Meta:
        model = PlaceReview
        fields = "__all__"
        read_only_fields = ["pk", "created", "updated", "user", "place"]

    def create(self, validated_data):
        request = self.context.get("request")
        place = self.context.get("place")
        review = PlaceReview.objects.create(
            **validated_data, user=request.user, place=place
        )
        return review
