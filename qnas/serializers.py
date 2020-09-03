from rest_framework import serializers

from .models import PlaceQuestion, PlaceReply

from places.serializers import RelationPlaceSerializer
from users.serializers import RelationUserSerializer


class QuestionSerializer(serializers.ModelSerializer):

    place = RelationPlaceSerializer(read_only=True)
    user = RelationUserSerializer(read_only=True)

    class Meta:
        model = PlaceQuestion
        exclude = ["is_active"]
        read_only_fields = ["place", "user", "pk", "created", "updated"]

    def create(self, validated_data):
        request = self.context.get("request")
        place = self.context.get("place")
        question = PlaceQuestion.objects.create(
            **validated_data, user=request.user, place=place
        )
        return question


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceReply
        exclude = ["is_active"]
        read_only_fields = ["pk", "question", "host", "created", "updated"]

    def create(self, validated_data):
        request = self.context.get("request")
        question = self.context.get("question")
        reply = PlaceReply.objects.create(
            **validated_data, host=request.user, question=question
        )
        return reply
