from django.core.management import BaseCommand

from main.models import Product


class Command(BaseCommand):
    Product.objects.all().delete()

    def handle(self, *args, **options):
        products_list = [{'name': 'orange', 'description': 'orange', 'category_id': 7, 'price': 13},
                         {'name': 'apple', 'description': 'apple', 'category_id': 7, 'price': 21}]

        for item in products_list:
            Product.objects.create(**item)
