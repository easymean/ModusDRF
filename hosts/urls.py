from django.urls import path, include
from . import views

app_name = "hosts"

host_list = views.HostViewSet.as_view({"post": "create", "get": "list"})
host_detail = views.HostViewSet.as_view({"get": "retrieve", "delete": "destroy"})

urlpatterns = [
    path("", host_list),
    path("<int:pk>", host_detail),
    path("login", views.LoginView.as_view()),
    path("admin", views.AdminCreateView.as_view()),
]
