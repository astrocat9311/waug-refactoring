import random
from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import ProductOption, Product

class Command(BaseCommand):
    help = 'This command creates test data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many data do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get('number')

        seeder = Seed.seeder()
        fake   = Faker(["ko_KR"])

        seeder.add_entity(ProductOption, 20, {
            'option' : lambda x: fake.ean13(), ## 바코드 형식의 무작위 데이터를 생성합니다.
            'price'  : fake.pydecimal(left_digits=6, right_digits=2, positive=True, min_value=1, max_value=None),
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('product_option data created'))