from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from placeReservations import views as reserviews

app_name = "places"

place_list = views.PlaceViewSet.as_view({"post": "create", "get": "list"})
place_detail = views.PlaceViewSet.as_view(
    {"get": "retrieve", "delete": "destroy", "put": "update"}
)

reservation_list = reserviews.ReservationViewSet.as_view(
    {"post": "create", "get": "list"}
)

resevervation_detail = reserviews.ReservationViewSet.as_view(
    {"get": "retrieve", "delete": "destroy"}
)


urlpatterns = [
    path("", place_list),
    path("<int:pk>/", place_detail),
    path("<int:place_pk>/reservations/", reservation_list),
    path("<int:place_pk>/reservations/<int:pk>/", resevervation_detail),
]
