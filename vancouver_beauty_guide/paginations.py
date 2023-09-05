from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CompanyPagination(BasePagination):
    pass


class CategoryPagination(BasePagination):
    pass


class ReviewPagination(BasePagination):
    pass
