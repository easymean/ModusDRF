from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "placeReservations"


urlpatterns = [
    path("<int:pk>/", views.ReadDeleteReservaionView.as_view()),
]
