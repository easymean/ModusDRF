from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import permissions


class ListPagination(PageNumberPagination):
    page_size = 10

