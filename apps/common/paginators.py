# Third-party imports.
from rest_framework.pagination import PageNumberPagination


class SmallPaginator(PageNumberPagination):
    page_size = 6


class MediumPaginator(PageNumberPagination):
    page_size = 10


class LargePaginator(PageNumberPagination):
    page_size = 15
