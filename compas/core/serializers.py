from rest_framework import serializers

from .models import Category, Company, Review, User


class UserSerializer(serializers.ModelSerializer):
    extra_kwargs = {'password': {'write_only': True}}

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Company
        exclude = ('id', 'is_verify')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categories'] = [category.name for category in instance.categories.all()]
        return response


class CompanyUpdateSerializer(CompanySerializer):
    class Meta:
        model = Company
        exclude = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    rating = serializers.ChoiceField(choices=RATING_CHOICES, required=True)

    class Meta:
        model = Review
        exclude = ('id', 'company', 'user')
