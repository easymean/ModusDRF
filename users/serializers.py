from rest_framework import serializers

from .models import User


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

    def validate_emIl(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Email alreay exists")

    def validate(self, data):
        # email = data.get("email", None)

        # if email is None:
        #     raise serializers.ValidationError("Email must be filled")

        # if email in User.objects.values_list("email", flat=True):
        #     raise serializers.ValidationError("email already exist")

        password = data.get("password", None)
        confirmed_password = data.get("confirmed_password", None)

        if password is None or confirmed_password is None:
            raise serializers.ValidationError("Password must be filled")

        if password != confirmed_password:
            raise serializers.ValidationError("Passwords don't match")

        return data

    def create(self, validated_data):
        group = self.context.get("group")

        if group == "user":
            return User.objects.create(
                email=validated_data["email"],
                password=validated_data["password"],
                username=validated_data["username"],
            )
        else:
            return User.objects.create_superuser(
                email=validated_data["email"],
                password=validated_data["password"],
                username=validated_data["username"],
            )


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

