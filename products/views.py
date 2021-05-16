import json

from django.views import View
from .models      import * #필요한 것만 가져오도록.
from users.models import User

from django.http  import JsonResponse
from utils        import login_required

class CategoryView(View):
    #모든 뷰에서 패스패러미터를 사용할 때 필요한 아이디가 없다...
    ## 에러처리 필요한 부분에 대해서 유의
    ### :8000/category/1/destination
    ### :8000/products/1
    ### 패스 파라미터 헷갈리지 않게...
    def get(self, request,category_id):
       category = Category.objects.get(id=category_id)
       data = {
           'name'     : category.name,
           'image_url': category.image_url
       }

       return JsonResponse({'data':data},status=200)

class DestinationView(View):
    def get(self,request,category_id):
        ## 또 id가 빠졌다...
        if not category_id or not Category.objects.get(id=category_id).exists():
            return JsonResponse({'message':'BAD_REQUEST'}, status=400)

        data = [{
            'name': destination.name,
            'image_url': destination.image_url
        } for destination in Category.objects.get(id=category_id).destination.all()]

        return JsonResponse({'data':data},status=200)

class ProductView(View):
    def get(self,request):
        print(json.loads(request.body))
        is_room     = request.GET.get('is_room',None)
        is_dinning  = request.GET.get('is_dinning',None)
        is_activity = request.GET.get('is_activity',None)

        if is_dinning:

            data = [{

                'name' : restaurant.name,
                'image': restaurant.productimage_set.all().first().image_url,
                'price': restaurant.price,
                'star_review':

            } for restaurant in Product.objects.filter(is_dinning=True)]

        if is_room:

            data = [{
                'name'       : room.name,
                'image'      : room.productimage_set.all().first().image_url,
                'price'      : room.price,
                'star_rating': room.star_rating,
                'rating'     : room.rating,
                'city'       : room.city.name,
                'district'   : room.district.name,

            } for room in Product.objects.filter(is_room=True)]

        if is_activity:

            data = [{
                'name'      : activity.name,
                'image'     : activity.productimage_set.all().first().image_url,
                'price'     : activity.price,
                'star_review': activity.star_review,
            } for activity in Product.objects.filter(is_activity==True)]

        return JsonResponse({'data':data},status=200)


class ProductDetailView(View):
    def get(self,request,product_id):

        if not product_id or not Product.objects.get(id=product_id).exists():
            return JsonResponse({'message':'BAD_REQUEST'}, status=400)

        product = Product.objects.get(id=product_id)

        if product.is_dinning == True: #이거는 불필

            data = {

                'name'          : product.name,
                'rating'        : product.rating,
                'description'   : product.description,
                'address'       : product.address,
                'latitude'      : product.latitude,
                'longitude'     : product.longitude,
                'city'          : product.city.name,
                'district'      : product.district.name,
                'price'         : product.price,
                'dinning_type'  :
                'dinning_option':
                'image_url'     : [image.image_url for image in product.productimage_set.all()]

                }

        if product.is_room == True:

            data = {
                'name'       : product.name,
                'rating'     : product.rating,
                'room'       : product.description,
                'address'    : product.address,
                'latitude'   : product.latitude,
                'longitude'  : product.longitude,
                'category'   : product.category.name,
                'city'       : product.city.name,
                'district'   : product.district.name,
                'price'      : product.price,
                'star_rating': Room.objects.get(id=product_id).star_rating,
                'convenience': [convenience.name for convenience in Room.objects.get(id=product_id).convenience.all()],
                'room_type'  : Room.objects.get(id=product_id).room_type,
                'image_url'  : [image.image_url for image in product.productimage_set.all()]

                }

        if product.is_activity == True:

            data = {
                'name': product.name,
                'rating': product.rating,
                'address': product.address,
                'description': product.description,
                'city': product.city.name,
                'district': product.district.name,
                'price': product.price,

            }

        return JsonResponse({'data':data},status=200)

class ReviewView(View):
    @login_required
    def post(self,request):
        data = json.loads(request.body)

        dinning_name  = data['dinning_name']
        user_email    = data['user_email']
        comment       = data['comment']
        star_rating   = data['star_rating']

        Review.objects.create(
            dinning_id  = Product.objects.get(name=dinning_name).id,
            user_id     = User.objects.get(email=user_email).id,
            comment     = comment,
            star_rating = star_rating
        )

        return JsonResponse({'message':'REVIEW_POSTED'}, status=201)

    def get(self,request, product_id):
        is_dinning = request.GET.get('is_dinning',None)

        restaurant = Product.objects.get(id=product_id,is_dinning=True)

        data = {

        }




