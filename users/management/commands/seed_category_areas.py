import random

from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import *


class Command(BaseCommand):
    help = 'This command creates test data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many data do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()

        seeder.add_entity(CategoryArea, 40, {
            'category': lambda x: random.choice(Category.objects.all()),
            'area'    : lambda x: random.choice(Area.objects.all())
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('category_area data created'))