from rest_framework import serializers

from .models import User
from common.mails import account_activation_token

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage


class RelationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "email")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "email", "username", "phone_number", "is_superuser")
        read_only_field = "pk"


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirmed_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "username") + ("password", "confirmed_password")

    def validate_email(self, value):
        existing = User.objects.filter(email=value).first()
        if existing:
            raise serializers.ValidationError("Email alreay exists")
        return value

    def validate(self, data):
        password = data["password"]
        confirmed_password = data["confirmed_password"]

        if password is None or confirmed_password is None:
            raise serializers.ValidationError("Password must be filled")

        if password != confirmed_password:
            raise serializers.ValidationError("Passwords don't match")

        return data

    def create(self, validated_data):
        group = self.context.get("group")
        meta = self.context.get("meta")

        confirmed_password = validated_data.pop("confirmed_password")

        if group == "user":
            user = User.objects.create(**validated_data)

        else:
            user = User.objects.create_superuser(**validated_data)

            user.email_verified = False

        user.save()
        message = render_to_string(
            "users/account_activate_email.html",
            {
                "user": user,
                "uid64": urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                "domain": meta,
                "token": account_activation_token.make_token(user),
            },
        )

        mail_subject = "test"
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

