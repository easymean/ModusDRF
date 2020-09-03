from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from .serializers import QuestionSerializer, ReplySerializer
from .models import PlaceQuestion, PlaceReply
from places.models import Place


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self, request, *args, **kwargs):
        place = Place.objects.filter(pk=self.kwargs["place_pk"], is_active=True)
        return PlaceQuestion.objects.filter(place=place, is_active=True)

    def create(self, request, **kwargs):
        place = self.kwargs["place_pk"]
        place = Place.objects.filter(pk=place, is_active=True).first()
        serializer = QuestionSerializer(
            data=request.data, context={"request": request, "place": place}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        question.is_active = False
        question.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)


class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class = ReplySerializer

    def get_queryset(self, request, *args, **kwargs):
        ques = PlaceQuestion.objects.filter(
            pk=self.kwargs["question_pk"], is_active=True
        )
        return ReplySerializer.objects.filter(question=ques, is_active=True)

    def create(self, request, **kwargs):
        ques = self.kwargs["question_pk"]
        ques = PlaceQuestion.objects.filter(pk=ques, is_active=True).first()
        serializer = ReplySerializer(
            data=request.data, context={"request": request, "question": ques}
        )
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        reply = self.get_object()
        reply.is_active = False
        reply.save()
        return Response(data={"result": "success"}, status=status.HTTP_204_NO_CONTENT)
