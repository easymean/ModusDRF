from rest_framework import serializers

from .models import PlaceReservation

from places.serializers import RelationPlaceSerializer
from users.serializers import RelationUserSerializer


class ListReservationSerializer(serializers.ModelSerializer):

    place = RelationPlaceSerializer(read_only=True)
    guest = RelationUserSerializer(read_only=True)

    class Meta:
        model = PlaceReservation
        fields = ["pk", "date", "place", "is_allowed", "check_in", "check_out", "guest"]


class PlaceReservationSerializer(serializers.ModelSerializer):
    place = RelationPlaceSerializer(read_only=True)
    guest = RelationUserSerializer(read_only=True)

    class Meta:
        model = PlaceReservation
        exclude = ["is_active", "updated"]
        read_only_fields = [
            "guest",
            "pk",
            "place",
            "created",
            "is_allowed",
        ]

    def validate(self, data):
        check_in = data.get("check_in")
        check_out = data.get("check_out")

        if check_in > check_out:
            raise serializers.ValidationError("wrong time set")

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        place = self.context.get("place")
        reservation = PlaceReservation.objects.create(
            **validated_data, guest=request.user, place=place
        )
        return reservation

