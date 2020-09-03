from django.urls import path, include

from . import views

app_name = "placeReviews"

urlpatterns = [
    path("<int:pk>", views.ReadUpdateDeleteReviewView.as_view()),
]

