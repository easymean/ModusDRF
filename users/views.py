import jwt, traceback, datetime

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status, permissions, generics, exceptions, serializers

from .models import User
from common.mails import account_activation_token
from .serializers import RegisterUserSerializer, UserSerializer, LoginSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == "create":
            return RegisterUserSerializer
        else:
            return UserSerializer

    def create(self, request):
        serializer = RegisterUserSerializer(
            data=request.data,
            context={"group": "user", "meta": request.META["HTTP_HOST"]},
        )
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destory(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)


class Activate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, uid64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uid64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        try:
            if user is not None and account_activation_token.check_token(user, token):
                user.email_verified = True
                user.save()

                return Response(
                    data={"email": user.email, "message": "회원가입이 완료되었습니다."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    data={"message": "만료된 링크입니다."}, status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            print(traceback.format_exc())


class LoginView(generics.GenericAPIView):
    permission_class = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email, is_active=True).first()
        if user is None:
            raise exceptions.AuthenticationFailed("user not found")

        if not user.check_pwd(input=password):
            raise exceptions.AuthenticationFailed("wrong password")

        encoded_jwt = jwt.encode(
            {"pk": user.pk, "group": "user"}, settings.SECRET_KEY, algorithm="HS256"
        )

        # response = Response(data={"token": encoded_jwt, "id": user.pk})
        # expiration = datetime.datetime.now() + settings.JWT_EXPIRATION_DELTA
        # response.set_cookie(
        #     settings.JWT_AUTH_COOKIE, encoded_jwt, expires=expiration, httponly=True
        # )
        # return response
        return Response(data={"token": encoded_jwt, "id": user.pk})


@api_view(["GET"])
def logout(request):
    response = Response(data={"message": "로그아웃되었습니다."}, status=status.HTTP_200_OK)
    response.set_cookie(settings.JWT_AUTH_COOKIE, " ")
    return response


class AdminCreateView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.none()

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(
            data=request.data, context={"group": "admin"}
        )
        try:
            serializer.is_valid(raise_exception=True)

        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST,)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
