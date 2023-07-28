from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from django.db.models import QuerySet

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page-size'
    max_page_size = 50

    def paginate_queryset(self, queryset: QuerySet, request, view=None):
            try:
                response = super().paginate_queryset(queryset, request, view)
            except NotFound:
                page_size = self.get_page_size(request)
                paginator = self.django_paginator_class(queryset, page_size)
                self.page = paginator.page(1)
                self.request = request
                response = []
            return response
