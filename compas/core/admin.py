from django.contrib import admin

from .models import Category, Company, Review, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Review)
