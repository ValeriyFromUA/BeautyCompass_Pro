from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=1000, blank=True)
    instagram = models.CharField(max_length=1000, blank=True)
    facebook = models.CharField(max_length=1000, blank=True)
    website = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    area = models.CharField(max_length=200, blank=True)
    is_verify = models.BooleanField(default=False)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0
    )

    def average_rating(self):
        average = self.review_set.aggregate(Avg('rating'))['rating__avg']
        return average if average is not None else 0.0

    def update_average_rating(self):
        average = self.review_set.aggregate(Avg('rating'))['rating__avg']
        self.rating = average if average is not None else 0.0
        self.save()

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.company.update_average_rating()

    def delete(self, *args, **kwargs):
        company = self.company
        super().delete(*args, **kwargs)

        company.update_average_rating()

    def __str__(self):
        return f"Review by {self.user.username} for {self.company.name}"
