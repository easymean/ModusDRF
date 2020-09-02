from rest_framework.response import Response
from rest_framework import viewsets, serializers, status, generics

from .models import PlaceReview
from .serializers import ReviewSerializer
from places.models import Place


class ReviewViewSet(viewsets.ModelViewSet):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        place = Place.objects.filter(pk=self.kwargs["place_pk"], is_active=True)
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


class ReadUpdateDeleteReviewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaceReview.objects.filter(is_active=True)
    serializer_class = ReviewSerializer

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        review.is_active = False
        review.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)
