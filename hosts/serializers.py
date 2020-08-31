import bcrypt
from rest_framework import serializers
from .models import Host


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ("pk", "email", "username", "phone_number", "is_superuser")
        read_only_field = "pk"


class RegisterHostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirmed_password = serializers.CharField(write_only=True)

    class Meta:
        model = Host
        fields = ("email", "username") + ("password", "confirmed_password")

    def create(self, validated_data):
        group = self.context.get("group")

        if group == "host":
            return Host.objects.create(
                email=validated_data["email"],
                password=validated_data["password"],
                username=validated_data["username"],
            )
        else:
            return Host.objects.create_superhost(
                email=validated_data["email"],
                password=validated_data["password"],
                username=validated_data["username"],
            )

    def validate(self, data):
        email = data.get("email", None)

        if email is None:
            raise serializers.ValidationError("Email must be filled")

        if email in Host.objects.values_list("email", flat=True):
            raise serializers.ValidationError("email already exist")

        password = data.get("password", None)
        confirmed_password = data.get("confirmed_password", None)

        if password is None or confirmed_password is None:
            raise serializers.ValidationError("Password must be filled")

        if password != confirmed_password:
            raise serializers.ValidationError("Passwords don't match")

        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
