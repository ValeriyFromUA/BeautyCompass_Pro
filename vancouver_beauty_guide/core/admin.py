from django.contrib import admin

from .models import User, Category, Company, Review

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Review)
