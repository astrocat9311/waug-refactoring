import random

from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import Room,RoomImage


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

        seeder.add_entity(RoomImage, 100, {
            'image_url': lambda x: fake.image_url,
            'room': random.choice(Room.objects.all())
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('data created'))