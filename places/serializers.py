from rest_framework import serializers

from .models import Place
from hosts.serializers import HostSerializer


class PlaceViewSetSerializer(serializers.ModelSerializer):

    host = HostSerializer(read_only=True)
    avg_rating = serializers.SerializerMethodField("get_avg_rating")

    class Meta:
        model = Place
        exclude = [
            "is_active",
            "location_code",
        ]
        read_only_fields = ["host", "pk", "created", "upated", "instant_book"]

    def validate(self, data):
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")

        if check_in > check_out:
            raise serializers.ValidateError("wrong time set")

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        place = Place.objects.create(**validated_data, host=request.user)
        return place

    def get_avg_rating(self, obj):
        return obj.get_total_rating()


class RelationPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["pk", "name", "address"]

