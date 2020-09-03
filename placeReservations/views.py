from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework import permissions, status, serializers

from .models import PlaceReservation
from .serializers import ReservationSerializer, ListReservationSerializer

from places.models import Place
from common.permissions import IsOwner
from common.paginations import OwnPagination

# url place/:id/reserv/:id/
class ReservationViewSet(ModelViewSet):
    pagination_class = OwnPagination()

    def get_permission(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:  # 수정 필요 place owner인 경우에만?
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        place = Place.objects.filter(pk=self.kwargs["place_pk"], is_active=True).first()
        return PlaceReservation.objects.filter(place=place, is_active=True)

    def get_serializer_class(self):
        if self.action == "list":
            return ListReservationSerializer
        else:
            return ReservationSerializer

    def create(self, request, *args, **kwargs):
        place_id = self.kwargs["place_pk"]
        place = Place.objects.filter(pk=place_id, is_active=True).first()
        serializer = ReservationSerializer(
            data=request.data, context={"request": request, "place": place}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        reserv = self.get_object()
        reserv.is_active = False
        reserv.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)


# reserv/:id/
class ReadDeleteReservaionView(RetrieveDestroyAPIView):
    queryset = PlaceReservation.objects.filter(is_active=True)
    serializer_class = ReservationSerializer

    def destroy(self, request, *args, **kwargs):
        reserv = self.get_object()
        reserv.is_active = False
        reserv.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)
