import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import status, permissions, generics, exceptions, serializers

from common.permissions import IsSelf
from .models import Host
from .serializers import RegisterHostSerializer, HostSerializer, LoginSerializer


class HostViewSet(ModelViewSet):
    queryset = Host.objects.filter(is_active=True)

    # def get_permissions(self):
    #     custom_permission_classes = []
    #     if self.action == "create":
    #         custom_permission_classes = [permissions.AllowAny]
    #     elif self.action == "retrieve" or self.action == "list":
    #         custom_permission_classes = [permissions.AllowAny]
    #     else:
    #         custom_permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in custom_permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return RegisterHostSerializer
        else:
            return HostSerializer

    def create(self, request):
        serializer = RegisterHostSerializer(
            data=request.data, context={"group": "host"}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destory(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)


class LoginView(generics.GenericAPIView):
    permission_class = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = Host.objects.filter(email=email, is_active=True).first()
        if user is None:
            raise exceptions.AuthenticationFailed("user not found")

        if not user.check_pwd(input=password):
            raise exceptions.AuthenticationFailed("wrong password")

        encoded_jwt = jwt.encode(
            {"pk": user.pk, "group": "host"}, settings.SECRET_KEY, algorithm="HS256"
        )
        return Response(data={"token": encoded_jwt, "id": user.pk})

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class AdminCreateView(generics.CreateAPIView):
    serializer_class = RegisterHostSerializer
    queryset = Host.objects.none()

    def post(self, request, *args, **kwargs):
        serializer = RegisterHostSerializer(
            data=request.data, context={"group": "admin"}
        )
        try:
            serializer.is_valid(raise_exception=True)

        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST,)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
