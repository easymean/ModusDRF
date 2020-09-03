from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import serializers, status, permissions

from .models import PlaceReview
from .serializers import ReviewSerializer
from places.models import Place
from common.permissions import IsOwner


class ReviewViewSet(ModelViewSet):

    serializer_class = ReviewSerializer

    def get_permission(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:  # delete and update
            permission_classes = [IsOwner, permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        place = Place.objects.filter(pk=self.kwargs["place_pk"], is_active=True).first()
        return PlaceReview.objects.filter(place=place, is_active=True)

    def create(self, request, *args, **kwargs):
        place_id = self.kwargs["place_pk"]
        place = Place.objects.filter(pk=place_id, is_active=True).first()
        serializer = ReviewSerializer(
            data=request.data, context={"request": request, "place": place}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        review.is_active = False
        review.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)


class ReadUpdateDeleteReviewView(RetrieveUpdateDestroyAPIView):
    queryset = PlaceReview.objects.filter(is_active=True)
    serializer_class = ReviewSerializer

    def get_permission(self):
        if self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        review.is_active = False
        review.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)
