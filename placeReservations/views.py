from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework import permissions, status, generics

from .models import PlaceReservation
from .serializers import PlaceReservationSerializer, ListReservationSerializer

from places.models import Place

# url place/:id/reserv/:id/
class ReservationViewSet(viewsets.ModelViewSet):
    def get_permission(self):
        pass

    def get_queryset(self):
        place = Place.objects.filter(pk=self.kwargs["place_pk"], is_active=True).first()
        return PlaceReservation.objects.filter(place=place, is_active=True)

    def get_serializer_class(self):
        if self.action == "list":
            return ListReservationSerializer
        else:
            return PlaceReservationSerializer

    def create(self, request, *args, **kwargs):
        place_id = self.kwargs["place_pk"]
        place = Place.objects.filter(pk=place_id).first()
        serializer = PlaceReservationSerializer(
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
class ReadDeleteReservaionView(generics.RetrieveDestroyAPIView):
    queryset = PlaceReservation.objects.filter(is_active=True)
    serializer_class = PlaceReservationSerializer

    def destroy(self, request, *args, **kwargs):
        reserv = self.get_object()
        reserv.is_active = False
        reserv.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)
