from rest_framework import serializers
from .models import Class


class ClassViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = [
            "is_active",
            "location_code",
        ]
        read_only_fields = [
            "somm",
            "pk",
            "created",
            "updated",
            "is_finished",
            "is_allowed",
        ]

    def validate(self, data):
        if self.instance:
            start = data.get("start_time", self.instance.start_time)
            end = data.get("end_time", self.instance.end_time)
        else:
            start = data.get("start_time")
            end = data.get("end_time")

        if start > end:
            raise serializers.ValidateError("wrong date")

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        new_class = Class.objects.create(**validated_data, somm=request.user)
        return new_class


class CreateOrUpdateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = [
            "is_finished",
            "is_allowed",
            "is_active",
            "created",
            "updated",
            "location_code",
        ]
        read_only_fields = ["somm"]

    def validate(self, data):
        if self.instance:
            start = data.get("start_time", self.instance.start_time)
            end = data.get("end_time", self.instance.end_time)
        else:
            start = data.get("start_time")
            end = data.get("end_time")

        if start > end:
            raise serializers.ValidateError("wrong date")

        return data

    def create(self, validated_data):
        a_class = Class.objects.create(**validated_data)
        return a_class


class DetailClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = ["is_allowed", "updated"]


class ListClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        include = ["pk", "title", "start_time", "price"]

    def validate(self, data):
        pass
