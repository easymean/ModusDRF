from django.urls import path, include

from . import views

app_name = "qnas"

reply_list = views.ReplyViewSet.as_view({"get": "list", "post": "create"})
reply_detail = views.ReplyViewSet.as_view({"get": "retrive", "delete": "destroy"})

urlpatterns = [
    path("<int:question_pk>/replies", reply_list),
    path("<int:question_pk>/replies/<int:pk>", reply_detail),
]

