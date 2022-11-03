from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "pagina"
    max_page_size = 15
    page_size_query_param = "total_resultados"
