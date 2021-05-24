import random

from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import Service,Room,ServiceCategory


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

        seeder.add_entity(Service, 80, {
            'name'            : lambda x: fake.word(),
            'service_category': lambda x: random.choice(ServiceCategory.objects.all())
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('services created'))

