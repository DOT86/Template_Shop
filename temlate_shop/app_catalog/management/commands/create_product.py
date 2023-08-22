from django.core.management import BaseCommand

from app_catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        for index in range(5, 1000):
            product = Product.objects.get_or_create(
                name=f'test{index}',
                price=index
            )
            product.description = f'description{index}'
            product.stock = index
            product.available = True
        self.stdout.write('good')

    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')
    # subcategory = ChainedForeignKey(SubCategory, chained_field="category", chained_model_field="category", show_all=False,
    #                              auto_choose=True, verbose_name='Название подкатегории',
    #                                 related_name='products') # type: ignore
    #
    # slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL товара')
    # image = models.ImageField(null=True, blank=True, verbose_name='Картинка')