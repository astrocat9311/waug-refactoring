import json

from django.test         import TestCase,Client
from products.models     import *

client = Client()

class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.bulk_create([
            Category(name= 'category1',image_url = 'category1.jpg'),
            Category(name= 'category2',image_url = 'category2.jpg')
        ])

    def tearDown(self):
        Category.objects.all().delete()

    def test_Category_Query_Success(self):
        response = client.get('/products/category')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{'data': [
            {'name': 'category1', 'image_url': 'category1.jpg'},
            {'name': 'category2', 'image_url': 'category2.jpg'}
                ]
            }
        )

class AreaTest(TestCase):
    def setUp(self):
        Area.objects.bulk_create([
            Area(name='area1',image_url='area1.jpg'),
            Area(name='area2',image_url='area2.jpg')
            ])

    def tearDown(self):
        Area.objects.all().delete()

    def test_Area_Query_Success(self):
        response = client.get('/products/area',)
        self.assertEqual(response.status_code,200)

class RoomDetailTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name      = 'category1',
            image_url = 'category1.jpg'
        )
        area = Area.objects.create(
            name      = 'area1',
            image_url = 'area1.jpg'
        )
        city = City.objects.create(
            name='city1'
        )
        district = District.objects.create(
            name = 'district1',
            city = city
        )
        room_type = RoomType.objects.create(
            name = 'roomtype1'
        )

        room = Room.objects.create(
            name        = 'room1',
            rating      = 8,
            grade       = 5,
            description = 'this is room1',
            address     = 'busan, haeundae',
            latitude    = -78.83339100000000000,
            longitude   = -96.62125200000000000,
            category    = category,
            area        = area,
            city        = city,
            district    = district,
            price       = 100000,
            type        = room_type
        )

        room_image1 = RoomImage.objects.create(
            image_url = 'RoomImage1.jpg',
            room = room
        )

        room_image2 = RoomImage.objects.create(
            image_url = 'RoomImage2.jpg',
            room = room
            )
    def tearDown(self):
        Category.objects.all().delete()
        Area.objects.all().delete()
        City.objects.all().delete()
        District.objects.all().delete()
        RoomType.objects.all().delete()
        Room.objects.all().delete()
        RoomImage.objects.all().delete()


    def test_RoomDetail_Query_Success(self):
        response = client.get('/products/room/1')
        self.assertEqual(response.status_code,200)

class ProductDetailTest(TestCase):
    def setUp(self):
        category1 = Category.objects.create(
            name      = 'category1',
            image_url = 'category1.jpg'
        )
        category2 = Category.objects.create(
            name      = 'category2',
            image_url = 'category2.jpg'
        )
        area = Area.objects.create(
            name      = 'area1',
            image_url = 'area1.jpg'
        )
        city = City.objects.create(
            name='city'
        )
        district = District.objects.create(
            name = 'district',
            city = city
        )
        product_type = ProductType.objects.create(
            name     = 'product_type'
        )
        product = Product.objects.create(
            name        = 'product1',
            rating      = 8,
            description = 'this is a product1',
            address     = 'address',
            latitude    = -78.83339100000000000,
            longitude   = -78.83339100000000000,
            category    = category1,
            area        = area,
            city        = city,
            district    = district,
            price       = 20000,
            type        = product_type,
            )
        product_images = ProductImage.objects.bulk_create([
            ProductImage(image_url='product_image1.jpg',product=product),
            ProductImage(image_url='product_image2.jpg',product=product)
        ])
    def tearDown(self):
        pass

    def test_ProductDetail_Query_Success(self):
        response = client.get('/products/goods/1')
        print(response.json())
        self.assertEqual(response.status_code, 200)