import csv
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
        fake = Faker(["ko_KR"])
        fake2=Faker(["en_US"])

        #seeder.add_entity(City, 30, {
        #    'name': lambda x: fake.city()
        #})
        #print(0)
        #seeder.add_entity(District, 50, {
        #    'name': lambda  x: fake.borough(),
        #    'city': lambda  x: random.choice(City.objects.all())
        #})
        #print(1)
        #seeder.add_entity(CategoryDestination, 40, {
        #    'category': lambda x: random.choice(Category.objects.all()),
        #    'destination': lambda x: random.choice(Destination.objects.all())
        #})
        #print(2)
        #seeder.add_entity(Room, 50, {
        #    'grade'        : lambda x: random.randint(0,5),
        #    'type': lambda x: random.choice(RoomType.objects.all()),
        #})
        #
        #seeder.add_entity(RoomService,50, {
        #    'room': lambda x: random.choice(Room.objects.all()),
        #    'service': lambda x: random.choice(Service.objects.all()),
        #    'service_type': lambda x: random.choice(ServiceType.objects.all()),
        #})
        print(3)
        seeder.add_entity(Product,50, {
            'name': lambda  x: fake.company(),
            'rating': lambda x: fake.pyint(min_value=0, max_value=10, step=1),
            'address': lambda x: fake.address(),
            'description': lambda x: fake2.paragraph(nb_sentences=5),
            'latitude': lambda x: fake2.latitude(),
            'longitude': lambda x: fake2.longitude(),
            'category': lambda x: random.choice(Category.objects.all()),
            'destination': lambda x: random.choice(Destination.objects.all()),
            'city': lambda x: random.choice(City.objects.all()),
            'district': lambda x: random.choice(District.objects.all()),
            'price': lambda x: fake.pyint(min_value=0, max_value=1000000, step=1000),
            'is_room': 0,
            'dinning_type': lambda x: random.choice(DinningType.objects.all()),

            'is_dinning': 1,
            'is_activity':0,
            'is_popular': lambda x: random.choice(range(0, 2)),
        })
        seeder.execute()
        print(4)
        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))




