import os
import django
import csv
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.chdir("..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','waug.settings')
django.setup()

from products.models import *
from users.models    import *
#CSV_PATH_PRODUCTS = './Product.csv'

CSV_PATH_PRODUCTS = 'categories.csv'
print(0)
with open('./db_upload/categories.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Category.objects.create(
                name           = data['name'],
                image_url      = data['image_url'],
                )
print(1)

with open('./db_upload/destinations.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Destination.objects.create(
                name      = data['name'],
                image_url = data['image_url']
                )

with open('./db_upload/room_types.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        RoomType.objects.create(
                name = data['name']
                )

with open('./db_upload/service_types.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        ServiceType.objects.create(
                name = data['name']
                )

with open('./db_upload/services.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Service.objects.create(
                name            = data['name'],
                service_type_id = data['service_type_id']
                )

with open('./db_upload/dinning_types.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        DinningType.objects.create(
                name = data['name']
                )

with open('./db_upload/coupons.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Coupon.objects.create(
                name = data['name'],
                discount_rate = data['discount_rate'],
                )

with open('./db_upload/activity_types.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        ActivityType.objects.create(
            name = data['name']
        )