from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    CreateCompanyAPIView,
    CategoryAPIView, UpdateCompanyAPIView, ReviewAPIView,
)
from django.urls import path, include, re_path
from rest_framework import routers

urlpatterns = [
    path("companies/", CreateCompanyAPIView.as_view(), name="companies"),
    path("companies/<int:pk>", UpdateCompanyAPIView.as_view(), name="company"),
    path("companies/<int:pk>/reviews", ReviewAPIView.as_view(), name="reviews"),
    path("categories/", CategoryAPIView.as_view(), name="categories"),

]
