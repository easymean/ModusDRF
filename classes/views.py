from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet

from .models import Class
from .serializers import (
    DetailClassSerializer,
    CreateOrUpdateClassSerializer,
    ListClassSerializer,
    ClassViewSetSerializer,
)
from common.views import ListPagination


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.filter(is_active=True)
    serializer_class = ClassViewSetSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        deleted = self.get_object()
        deleted.is_active = False
        deleted.save()
        return Response(data={"result": "success"})


# class ClassView(APIView):
#     def get_class(self, id):
#         try:
#             a_class = Class.objects.get(pk=id, is_active=True)
#             return a_class
#         except Class.DoesNotExist:
#             return None

#     def post(self, request):
#         serializer = CreateOrUpdateClassSerializer(data=request.data)
#         print(request.user)
#         if serializer.is_valid():
#             a_class = serializer.save()
#             class_serializer = DetailClassSerializer(a_class).data
#             return Response(data=class_serializer, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, id):
#         a_class = self.get_class(id)
#         if a_class is not None:
#             serializer = DetailClassSerializer(a_class).data
#             return Response(serializer)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, id):
#         serializer = CreateOrUpdateClassSerializer(data=request.data)
#         if serializer.is_valid():
#             a_class = serializer.save()
#             class_serializer = DetailClassSerializer(a_class).data
#             return Response(data=class_serializer, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         a_class = self.get_class(id)
#         if a_class is not None:
#             a_class.is_active = False
#             a_class.save()
#             serializer = DetailClassSerializer(a_class).data
#             return Response(serializer)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class ListClassesView(APIView):
#     def get(self, request):
#         paginator = ListPagination()
#         classes = Class.objects.all(is_active=True)
#         results = paginator.paginate_queryset(classes, request)
#         serializer = ListClassSerializer(results, many=True).data
#         return paginator.get_paginated_response(serializer)
