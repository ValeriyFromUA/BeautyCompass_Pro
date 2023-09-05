from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.models import Company, Category, Review
from core.permissions import CategoryPermission, CompanyDetailsPermission
from core.serializers import CompanySerializer, CategorySerializer, ReviewSerializer, CompanyUpdateSerializer
from paginations import CompanyPagination, CategoryPagination, ReviewPagination


# Create your views here.
class CreateCompanyAPIView(ListCreateAPIView):
    queryset = Company.objects.filter(is_verify=True)
    serializer_class = CompanySerializer
    pagination_class = CompanyPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateCompanyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.filter(is_verify=True)
    serializer_class = CompanyUpdateSerializer
    permission_classes = [CompanyDetailsPermission]


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermission]
    pagination_class = CategoryPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ReviewPagination

    def create(self, request, *args, **kwargs):
        company = self.kwargs.get('pk')
        user = self.request.user
        data = self.request.data
        rating = data['rating']
        text = data['text']
        try:
            company = Company.objects.get(id=company)
        except Company.DoesNotExist:
            return Response({'error': 'Компанія з вказаним ID не знайдена'}, status=status.HTTP_404_NOT_FOUND)

        review = Review(user=user, company=company, text=text, rating=rating)
        review.save()
        return Response({'message': 'Відгук створено успішно'}, status=status.HTTP_201_CREATED)
