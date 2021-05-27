import json

from django.test         import TestCase,Client
from products.models     import *

client = Client()
class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(
            name      = 'hotel',
            image_url = 'category_url_testing.com'
        )

        Category.objects.create(

            name      = 'motel',
            image_url = 'category_url_testing.com'
        )

    def tearDown(self):
        Category.objects.all().delete()

    def test_Category_Query_Success(self):
        response = client.get('/products/category',)

        self.assertEqual(response.status_code,200)

class AreaTest(TestCase):
    def setUp(self):
        Area.objects.create(
            id        = 1,
            name      = 'Seoul',
            image_url = 'testing_urls'
        )
        Area.objects.create(
            id       = 2,
            name     = 'Busan',
            image_url='testing_urls'
        )

    def tearDown(self):
        Area.objects.all().delete()

    def test_Area_Query_Success(self):
        response = client.get('/products/area',)
        self.assertEqual(response.status_code,200)

class RoomDetailTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            id        = 1,
            name      = 'hotel',
            image_url = 'test_url1'
        )
        area = Area.objects.create(
            id        = 1,
            name      = 'busan',
            image_url = 'test_url2'
        )
        city = City.objects.create(
            id =1,
            name='busan'
        )
        district = District.objects.create(
            id      = 1,
            name    = 'haeundae',
            city_id = city.id
        )
        room_type = RoomType.objects.create(
            id   = 1,
            name = 'hostel'
        )

        room = Room.objects.create(
            name = 'BusanHotel',
            rating = 8,
            grade = 5,
            description = 'this is Busan Hotel',
            address = 'busan, haeundae',
            latitude = -78.83339100000000000,
            longitude = -96.62125200000000000,
            category_id = category.pk,
            area_id = area.pk,
            city_id = city.pk,
            district_id = district.pk,
            price = 100000,
            type_id = room_type.pk
        )

        room_image1 = RoomImage.objects.create(
            image_url = 'test_url_3',
            room_id = room.pk
        )

        room_image2 = RoomImage.objects.create(
            image_url = 'test_url_4',
            room_id = room.pk
            )

    def test_RoomDetail_Query_Success(self):
        response = client.get('/products/room/1')
        self.assertEqual(response.status_code,200)

class ProductDetailTest(TestCase):
    def setUp(self):
        category1 = Category.objects.create(
            name      = 'dinning',
            image_url = 'testing_url1'
        )
        category2 = Category.objects.create(
            name      = 'acttivity',
            image_url = 'testing_url0'
        )
        area = Area.objects.create(
            name      = 'Seoul',
            image_url = 'testing_url2'
        )
        city = City.objects.create(
            name='Seoul'
        )
        district = District.objects.create(
            name = 'gangnam',
            city = City.objects.get(name='Seoul')
        )
        product_type = ProductType.objects.create(
            name     = 'outdoor'
        )
        product = Product.objects.create(
            name        = 'hiking',
            rating      = 8,
            description = 'this is a hiking program',
            address     = 'Seoul, gangnam',
            latitude    = -78.83339100000000000,
            longitude   = -78.83339100000000000,
            category_id = category2.pk,
            area_id     = area.pk,
            city_id     = city.pk,
            district_id = district.pk,
            price       = 20000,
            type_id     = product_type.pk,
            )
        product_image1 = ProductImage.objects.create(
            image_url  = 'testing_url3',
            product_id = product.pk
        )
        product_image2 = ProductImage.objects.create(
            image_url  = 'testing_url4',
            product_id = product.pk
        )

    def test_ProductDetail_Query_Success(self):
        response = client.get('/products/goods/1')
        self.assertEqual(response.status_code, 200)