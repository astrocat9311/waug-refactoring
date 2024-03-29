import random

from faker                       import Faker
from django.core.management.base import BaseCommand
from django_seed                 import Seed
from products.models             import Room,Category,Area,City,District,RoomType,Service


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
        fake2  = Faker(["en_US"])

        seeder.add_entity(Room, 50, {
            'name'       : lambda x : fake.language_name(),
            'rating'     : lambda x : random.choice(range(11)),
            'grade'      : lambda x : random.choice(range(6)),
            'description': lambda x : fake.paragraph(nb_sentences=5),
            'address'    : lambda x : fake.address(),
            'latitude'   : lambda x : fake.latitude(),
            'longitude'  : lambda x : fake.longitude(),
            'category'   : lambda x : random.choice(Category.objects.all()),
            'area'       : lambda x : random.choice(Area.objects.all()),
            'city'       : lambda x : random.choice(City.objects.all()),
            'district'   : lambda x : random.choice(District.objects.all()),
            'price'      : lambda x : fake.pydecimal(left_digits=6, right_digits=2,positive=True, min_value=1),
            'is_popular' : lambda x : fake.boolean(chance_of_getting_true=50),
            'type'       : lambda x : random.choice(RoomType.objects.all()),
            'service'    : lambda x : random.choice(Service.objects.all())
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS('room data created'))
