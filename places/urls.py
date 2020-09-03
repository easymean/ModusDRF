from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from placeReservations import views as reserviews
from placeReviews import views as revviews
from qnas import views as qnaviews

app_name = "places"

place_list = views.PlaceViewSet.as_view({"post": "create", "get": "list"})
place_detail = views.PlaceViewSet.as_view(
    {"get": "retrieve", "delete": "destroy", "put": "update"}
)

reservation_list = reserviews.ReservationViewSet.as_view(
    {"post": "create", "get": "list"}
)

reservation_detail = reserviews.ReservationViewSet.as_view(
    {"get": "retrieve", "delete": "destroy"}
)

review_list = revviews.ReviewViewSet.as_view({"get": "list", "post": "create"})
review_detail = revviews.ReviewViewSet.as_view({"get": "retrieve", "delete": "destroy"})

ques_list = qnaviews.QuestionViewSet.as_view({"get": "list", "post": "create"})
ques_detail = qnaviews.QuestionViewSet.as_view({"get": "retrieve", "delete": "destroy"})

urlpatterns = [
    path("", place_list),
    path("<int:pk>", place_detail),
    path("<int:place_pk>/reservations", reservation_list),
    path("<int:place_pk>/reservations/<int:pk>", reservation_detail),
    path("<int:place_pk>/reviews", review_list),
    path("<int:place_pk>/reviews/<int:pk>", review_detail),
    path("<int:place_pk>/questions", ques_list),
    path("<int:place_pk>/questions/<int:pk>", ques_detail),
]
