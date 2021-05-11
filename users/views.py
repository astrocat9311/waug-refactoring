import bcrypt
import jwt
import json

from django.http            import JsonResponse, HttpResponse
from django.views           import View
from django.core.exceptions import ValidationError
from django.utils.crypto    import get_random_string

from utils        import validate_email,validate_password
from users.models import User, Coupon, UserCoupon, Wishlist
from my_settings  import SECRET_KEY,algorithm

class UserSignupView(View):
    def post(self,request):
       try:
            data = json.loads(request.body)

            email = data['email']
            name = data['name']
            password = data['password']

            if User.objects.filter(email=email).exists():
                return HttpResponse(status=409)

            if not email or not name or not password:
                return JsonResponse({'message':'NO_INPUTS'},status=400)

            if validate_email(email) and validate_password(password):
                hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

                user, is_new = User.objects.get_or_create(
                    email = email,
                    password = hashed_password,
                    name = name,
                )
                if is_new:
                    coupon = Coupon.objects.get(name='new member welcome')
                    UserCoupon.objects.create(code=get_random_string(length=10), user=user, coupon=coupon)

            return JsonResponse({'message':'SIGN_UP_SUCCESS'}, status=201)

       except KeyError:
           return JsonResponse({'message':'KEY_ERROR'}, status=400)

       except ValidationError as VE:
           return JsonResponse({'message':str(VE)},status=400)

class UserLoginView(View):
    def post(self,request):

        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not email or not password:
                return JsonResponse({'message':'CHECK_INPUTS'},status=400)

            if not User.objects.filter(email=email).exists():
                return HttpResponse(status=401)

            if not validate_email(email) or not validate_password(password):
                return JsonResponse({'message':'INVALID_INPUTS'}, status=400)

            user = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                access_token = jwt.encode({'id':user.id},SECRET_KEY,algorithm)
                return JsonResponse({'access_token':access_token},status=200)
            else:
                return HttpResponse(status=403)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class CouponView(View):
    def post(self,request):
        data = json.loads(request.body)

        name          = data['name']
        discount_rate = data['discount_rate']

        Coupon.objects.create(
            name          = name,
            discount_rate = discount_rate,
        )
        return JsonResponse({'message':'COUPON_ISSUED'},status=201)
