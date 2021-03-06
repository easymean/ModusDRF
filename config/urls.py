"""modus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/users/", include("users.urls")),
    path("v1/hosts/", include("hosts.urls")),
    # path("v1/somms/", include("somms.urls")),
    path("v1/places/", include("places.urls")),
    path("v1/classes/", include("classes.urls")),
    path("v1/place-reservations/", include("placeReservations.urls")),
    path("v1/place-reviews/", include("placeReviews.urls")),
    path("v1/questions/", include("qnas.urls")),
]
