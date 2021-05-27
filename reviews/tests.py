import json
import jwt
import bcrypt

from django.test        import (TestCase,Client)
from unittest.mock      import patch

from users.models       import *
from products.models    import *
from my_settings        import SECRET_KEY,algorithm

client = Client()

class ReviewTest(TestCase):
    def setUp(self):
        User.objects.bulk_create([
            User(name      = 'tester1',
                 email     = 'tester1@wecode.com',
                 password  = bcrypt.hashpw('Qwerty123!'.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"),
                 is_social = 0),

            User(name      = 'tester2',
                 email     = 'tester2@wecode.com',
                 password  = bcrypt.hashpw('Qwerty123!'.encode("utf-8"),bcrypt.gensalt()).decode("utf-8"),
                 is_social = 0)
        ])

        self.token1 = jwt.encode({'id':User.objects.get(name='tester1').id},SECRET_KEY,algorithm=algorithm)
        self.token2 = jwt.encode({'id':User.objects.get(name='tester2').id},SECRET_KEY,algorithm=algorithm)

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
             id          = 1,
             name        = 'product1',
             rating      = 8,
             description = 'this is a product1',
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
            "user_id"    : user.id,
            "comment"    : "nice",
            "rating"     : 8,
            "product_id" : 1,
            "image_url"  : ["test1.jpg","test2.jpg"]
        }

        response = client.post("/reviews/product/1", json.dumps(data),**header,content_type="application/json")
        self.assertEqual(response.status_code,201)