import bcrypt
import jwt
import json

from django.http            import JsonResponse, HttpResponse
from django.views           import View
from django.core.exceptions import ValidationError
from django.utils.crypto    import get_random_string

from utils           import validate_email,validate_password,login_required
from users.models    import User, Coupon, Wishlist
from my_settings     import SECRET_KEY,algorithm

class UserSignupView(View):
    def post(self,request):
       try:
            data = json.loads(request.body)

            email = data['email']
            name = data['name']
            password = data['password']

            if User.objects.filter(email=email).exists():
                return JsonResponse({},status=401)

            if not email or not name or not password:
                return JsonResponse({'message':'NO_INPUTS'},status=400)

            if validate_email(email) and validate_password(password):

                hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
                signup = User.objects.create(
                    name=name,
                    email=email,
                    password=hashed_password
                )

                signup.coupon.add(
                    Coupon.objects.create(
                        name='신규회원가입 쿠폰',
                        discount_rate=3000,
                        code=get_random_string(length=20))
                )

            return JsonResponse({'message': 'SIGN_UP_COMPLETE'}, status=201)
                #user, is_new = User.objects.get_or_create(
                #    email = email,
                #    password = hashed_password,
                #    name = name,
                #)
                #if is_new:
                #    coupon = Coupon.objects.get(name='신규 회원가입 축하 쿠폰')
                #    UserCoupon.objects.create(code=get_random_string(length=10), user=user, coupon=coupon)
                #
                #return JsonResponse({'message':'SIGN_UP_SUCCESS'}, status=201)

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
                return HttpResponse(status=404)

            if not validate_email(email) or not validate_password(password):
                return JsonResponse({'message':'INVALID_INPUTS'}, status=400)

            user = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                access_token = jwt.encode({'id':user.id},SECRET_KEY,algorithm)
                return JsonResponse({'access_token':access_token, },status=200)

            return HttpResponse(status=403)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class WishlistView(View):
    @login_required
    def post(self,request):
        data = json.loads(request.body)

        product_id = data['product_id']
        user_id    = request.user.id

        Wishlist.objects.create(
            product_id = product_id,
            user_id = user_id
        )

        return JsonResponse({'message':'SUCCESS'},status=201)

    @login_required
    def get(self, request):

        user = request.user
        print(user.email, user.name)
        print("testing", request.user)
        wishlists = Wishlist.objects.filter(user=user)
        print(wishlists)

        try:
            data = [{
                'name'     : wishlist.product.name,
                'price'    : wishlist.product.price,
                'image_url': wishlist.product.productimage_set.all().first(),

            } for wishlist in Wishlist.objects.filter(user=user)]

        except:
            return JsonResponse({'message':'EMPTY_WISHLIST'}, status=201)


        return JsonResponse({'data':data},status=200)








