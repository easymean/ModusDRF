from rest_framework.routers import DefaultRouter

from . import views

app_name = "classes"

router = DefaultRouter()
router.register("", views.ClassViewSet, basename="class")

urlpatterns = router.urls
