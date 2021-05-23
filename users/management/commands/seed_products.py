import random

from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import Category,City,Area,District,ProductType,Product


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


        seeder.add_entity(Product, 50, {
            'name'       : lambda x: fake.language_name(),
            'rating'     : lambda x: random.choice([x / 10 for x in range(0, 10)]),
            'description': lambda x: fake.paragraph(nb_sentences=5),
            'address'    : lambda x: fake.address(),
            'latitude'   : lambda x: fake.latitude(),
            'longitude'  : lambda x: fake.longitude(),
            'category'   : random.choice(Category.objects.all()),
            'area'       : random.choice(Area.objects.all()),
            'city'       : random.choice(City.objects.all()),
            'district'   : random.choice(District.objects.all()),
            'price'      : lambda x: fake.pydecimal(left_digits=6, right_digits=2, positive=True, min_value=1, max_value=None),
            'is_popular' : lambda x: fake.boolean(chance_of_getting_true=50),
            'type'       : random.choice(ProductType.objects.all())
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('data created'))