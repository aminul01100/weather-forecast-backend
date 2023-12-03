import csv
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Name of the query parameter for page size
    page_size = 10
    max_page_size = 100

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size:
            return int(page_size)
        return self.page_size
