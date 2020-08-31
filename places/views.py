from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Place
from .serializers import PlaceViewSetSerializer
from .permissions import IsHostAuthenticated

from common.permissions import IsOwner


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.filter(is_active=True)
    serializer_class = PlaceViewSetSerializer

    def get_permission(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
            # permission_classes = [IsHostAuthenticated]
        elif self.action == "create":
            permission_classes = [IsHostAuthenticated]
            # permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        place = self.get_object()
        place.is_active = False
        place.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)
