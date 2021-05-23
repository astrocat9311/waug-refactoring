import json
import jwt
import bcrypt

from unittest           import (TestCase,main)
from unittest.mock      import patch
from django.test        import Client

from users.models       import *
from products.models    import *
from my_settings        import SECRET_KEY,algorithm

client = Client()

class ReviewTest(TestCase):

    def setUp(self):
       user1 = User.objects.create(
            name      = 'tester1',
            email     = 'tester1@wecode.com',
            password  = bcrypt.hashpw('Qwerty123!'.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"),
            is_social = 0
        )
       user1.save()
       self.token1 = jwt.encode({'id':user1.id},SECRET_KEY,algorithm=algorithm)

       user2 = User.objects.create(
            name      = 'tester2',
            email     = 'tester2@wecode.com',
            password  = bcrypt.hashpw('Qwerty123!'.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"),
            is_social = 0
        )
       user2.save()
       self.token2 = jwt.encode({'id':user2.id},SECRET_KEY,algorithm=algorithm)

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

       district =  District.objects.create(

            name    = 'test_district',
            city_id = city.pk
       )

       type = ProductType.objects.create(

            name = 'test_product_type'
        )


       product = Product.objects.create(
            pk =2,
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
            is_popular  = 1,
            type_id     = type.pk
            )


    def tearDown(self):
        Category.objects.all().delete()
        Area.objects.all().delete()
        City.objects.all().delete()
        District.objects.all().delete()
        ProductType.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()

    def test_Review_post_success(self):
        header  = {"HTTP_Authorization": self.token1}
        token   = header["HTTP_Authorization"]
        payload = jwt.decode(token,SECRET_KEY,algorithms=algorithm)
        user    = User.objects.get(id=payload["id"])


        data = {
            "user_id"    : user.pk,
            "comment"    : "nice",
            "rating"     : 8,
            "product_id" : 2,
            "image_url"  : ["abcd","wxyz"]
        }

        response = client.post("/reviews/product/2", json.dumps(data),**header,content_type="application/json")
        self.assertEqual(response.status_code,201)