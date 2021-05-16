import os

import json
import bcrypt

from .models       import User
from django.test   import TestCase,Client
from unittest.mock import patch, MagicMock

class SignupTest(TestCase):
    def setUP(self):
        User.objects.create(
            name='kim',
            email = 'kim@wecode.com',
            password = 'Qwerty123!'

        )
    def tearDown(self):
        User.objects.get(name='kim').delete()

    def test_success_sigup(self):
        user = {

        }




