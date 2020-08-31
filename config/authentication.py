import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from users.models import User
from hosts.models import Host
from somms.models import Somm


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            group = decoded.get("group")

            if group == "user":
                user = User.objects.get(pk=pk)
            elif group == "host":
                user = Host.objects.get(pk=pk)
            else:
                user = Somm.objects.get(pk=pk)
            return (user, None)
        except (ValueError, User.DoesNotExist, Host.DoesNotExist, Somm.DoesNotExist):
            return None
        except jwt.exceptions.DecodeError:
            return exceptions.AuthenticationFailed(detail="JWT Format Invalid")
