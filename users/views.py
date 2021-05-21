import bcrypt
import jwt
import json
import requests

from django.http            import JsonResponse, HttpResponse
from django.shortcuts       import redirect
from django.views           import View
from django.core.exceptions import ValidationError
from django.utils.crypto    import get_random_string

from utils           import validate_email,validate_password,login_required
from users.models    import User, Coupon, Wishlist
from my_settings     import SECRET_KEY,algorithm,KAKAO_KEY

class UserSignupView(View):
    def post(self,request):
       try:
            data = json.loads(request.body)

            email = data['email']
            name = data['name']
            password = data['password']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'EMAIL_EXISTS'},status=409)

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

            user = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                access_token = jwt.encode({'id':user.id},SECRET_KEY,algorithm)
                return JsonResponse({'access_token':access_token,'message':'LOG_IN_SUCCESS'},status=200)

            else:
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

class KakaoLoginView(View):
    def get(self,request):
        client_id    = KAKAO_KEY
        redirect_uri = "http://127.0.0.1:8000/users/kakao/login/callback"

        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )


class KakaoLoginCallbackView(View):
    def get(self,request):
         
        print(request.GET)
        code          = request.GET.get("code")
        client_id     = KAKAO_KEY
        redirect_uri  = "http://127.0.0.1:8000/users/kakao/login/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&\
                redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()
        error      = token_json.get("error",None)
        print(error)

        if error is not None:
            return JsonResponse({'message':'INVALID_CODE'},status=400)
        else:
            access_token = token_json.get("access_token")
        print(access_token)
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}
        )
        #### call-back view는 이까지가 프론트에서 처리합니다.

        profile_json = profile_request.json()
        print(profile_json)

        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email",None)
        print(email)
        kakao_id = profile_json.get("id")
        print(kakao_id)

        if User.objects.filter(social_account = kakao_id).exists():
            user_kakao = User.objects.get(social_account = kakao_id)
            token = jwt.encode({"email":email},SECRET_KEY,algorithm)

            return JsonResponse({"message":"KAKAO_LOGIN_SUCCESS","token":token},status=200)

        else:
            User(social_account = kakao_id,
                 email=email,
                 is_social = True).save()


            token = jwt.encode({"email":email},SECRET_KEY,algorithm)

            return JsonResponse({"token":token},status=200)