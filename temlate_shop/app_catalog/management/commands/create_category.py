from django.core.management import BaseCommand

from app_catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        category = Category.objects.get_or_create(
            name="Книги", slug="catalog--book")
        self.stdout.write('good')