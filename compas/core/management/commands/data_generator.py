import csv
import os

import django
from django.core.management.base import BaseCommand

from constants import CATEGORIES
from core.models import Category, Company

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

django.setup()


class Command(BaseCommand):
    help = 'Generates companies and populates the database.'

    def handle(self, *args, **options):
        self.add_category()
        self.add_companies()

    @staticmethod
    def add_category():
        for category in CATEGORIES:
            Category.objects.create(name=category)

    @staticmethod
    def add_companies():
        with open('output.csv', mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                print(row)
                # Обробка рядка CSV-файлу та створення об'єкту Company
                name = row['name']
                categories = row['category'].split(', ')
                city = row['city']
                address = row['address']
                phone = row['phone']
                email = row['email']
                instagram = row['instagram']
                facebook = row['facebook']
                website = row['website']
                postal_code = row['postal_code']
                area = row['area']

                company = Company(
                    name=name,
                    city=city,
                    address=address,
                    phone=phone,
                    email=email,
                    instagram=instagram,
                    facebook=facebook,
                    website=website,
                    postal_code=postal_code,
                    area=area,
                    is_verify=True,
                )
                company.save()

                for category_name in categories:
                    category, _ = Category.objects.get_or_create(name=category_name)
                    company.categories.add(category)
