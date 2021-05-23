import json
import unittest
import bcrypt
import jwt
from django.test import (TestCase,Client)
from .models     import User
from my_settings import SECRET_KEY, algorithm

class SignUpTest(unittest.TestCase):
    def setUp(self):
        User.objects.create(
                name     = 'foo0',
                email    = 'foo0@wecode.com',
                password ='Qwerty123!')

    def tearDown(self):
        User.objects.all().delete()

    def test_success_signup(self):
        client = Client()
        data = {
                'email'   : 'foo1@wecode.com',
                'password': 'Qwerty123!',
                'name'    : 'foo1'
                }
        response = client.post('/users/signup', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : "SIGN_UP_COMPLETE"})

    def test_fail_email_exist(self):
        client = Client()
        data = {
                'email'   : 'foo0@wecode.com',
                'password': 'Qwerty123!',
                'name'    : 'foo1'
                }
        response = client.post('/users/signup', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), {'message' : 'EMAIL_EXISTS'})

    def test_email_validation_check(self):
        client = Client()
        data = {
                'email'    : 'foogmail.com',
                'password' : 'Qwerty123!',
                'name'     : 'foo'
                }
        response = client.post('/users/signup', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_password_validation_check(self):
        client = Client()
        data = {
                'email'   :'foo2@gmail.com',
                'password':'qreq',
                'name'    :'foo2'
                }
        response = client.post('/users/signup', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_signup_Key_Error(self):
        client=Client()
        data = {
            'emake'  : 'foo3@gmail.com',
            'passwor':'Qwerty123!',
            'nam'    :'foo3'
        }
        response = client.post('/users/signup',json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code,400)

class LoginTest(unittest.TestCase):
    def setUp(self):
        User.objects.create(
                email    = 'fizz0@wecode.com',
                password = bcrypt.hashpw('Qwerty123!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                name     = 'fizz0'
                )

    def tearDown(self):
        User.objects.all().delete()

    def test_success_login(self):
        client = Client()
        data = {
                'email'   : 'fizz0@wecode.com',
                'password': 'Qwerty123!'
                }

        user_test    = User.objects.get(email='fizz0@wecode.com')
        access_token = jwt.encode({'id': user_test.id}, SECRET_KEY, algorithm)

        response     = client.post('/users/login', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'access_token' : access_token,'message':'LOG_IN_SUCCESS'})

    def test_fail_login_no_inputs(self):
        client = Client()
        data = {
            "email"    : "",
            "password" : ""
        }
        response = client.post('/users/login',json.dumps(data),content_type='application/json')

        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(),{'message':'CHECK_INPUTS'})

    def test_fail_login_email_DoesNotExist(self):
        client = Client()
        data = {
                'email'    : 'fizz1@wecode.com',
                'password' : 'Qwerty123!'
                }
        response = client.post('/users/login', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_fail_login_password_mismatch(self):
        client = Client()
        data = {
                'email'   : 'fizz0@wecode.com',
                'password': 'Qwerty123!!'
                }
        response = client.post('/users/login', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 403)

    def test_fail_login_Key_Error(self):
        client = Client()
        data = {
            'emake'   :'fizz0@wecode.com',
            'p@ssword':'Qwerty123!'
        }

if __name__ == '__main__':
    unittest.main()

