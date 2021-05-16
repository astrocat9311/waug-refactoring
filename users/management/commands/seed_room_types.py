import csv
import random
from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import *
from django.utils.crypto         import get_random_string

class Command(BaseCommand):
    help = 'This command creates test data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many data do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        fake = Faker(["ko_KR"])
        fake2 = Faker(["en_US"])

        seeder.add_entity(RoomType, 10, {
            'name': lambda x: fake.word()
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('data created'))