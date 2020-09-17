from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "users"


user_list = views.UserViewSet.as_view({"post": "create", "get": "list"})
user_detail = views.UserViewSet.as_view({"get": "retrieve", "delete": "destroy"})
urlpatterns = [
    path("", user_list),
    path("<int:pk>", user_detail),
    path("admin", views.AdminCreateView.as_view()),
    path("login", views.LoginView.as_view()),
    path("logout", views.logout),
    path("activate/<str:uid64>/<str:token>", views.Activate.as_view(), name="activate"),
]
