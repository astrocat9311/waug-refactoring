import json
import unittest

from django.test         import (TestCase,Client)
from reviews.models      import Review,ReviewPhoto
from users.models        import *
from products.models     import *

client = Client()
class ReviewCreateTest(TestCase):
    @classmethod
    def setUpTestData(self):
        category = Category.objects.create(

            name      = 'test_category',
            image_url = 'testing_url'
        )

        area = Area.objects.create(

            name      = 'test_area',
            image_url = 'testing_url'
        )

        city = City.objects.create(

            name = 'test_city'
        )

        district = District.objects.create(

            name    = 'test_district',
            city_id = city.pk
        )

        type = ProductType.objects.create(
            name = 'test_product_type'
        )

        product = Product.objects.create(
            pk          = 1,
            name        = 'examination',
            rating      = 8,
            description = 'this is a testing',
            address     = '테헤란로 427',
            latitude    = 74.26290350000000000,
            longitude   = -122.07453700000000000,
            category_id = category.pk,
            area_id     = area.pk,
            city_id     = city.pk,
            district_id = district.pk,
            price       = 100000,
            is_popular  = True,
            type_id     = type.pk
            )

        user = User.objects.create(
            name     = 'buzz',
            email    = 'buzz@wecode.com',
            password = 'Qwerty123!'
        )
    def tearDown(self):
        Category.objects.all().delete()
        Area.objects.all().delete()
        City.objects.all().delete()
        District.objects.all().delete()
        ProductType.objects.all().delete()
        Product.objects.all().delete()

    def test_Review_post_success(self):
        data = {
            'product_id': Product.objects.get(pk=1).id,
            'user_id': User.objects.get(pk=1).id,
            'comment': 'testing testing testing',
            'rating':5,
            'image_url': ['testing_url1','testing_url2']
        }

        response = client.post('/reviews',json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,201)
