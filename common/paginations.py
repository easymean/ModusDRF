from rest_framework.pagination import PageNumberPagination


class OwnPagination(PageNumberPagination):
    page_size = 20
