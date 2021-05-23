import json

from json         import JSONDecodeError
from django.http  import JsonResponse
from django.views import View

from products.models import Product
from .models         import Review, ReviewPhoto
from utils           import login_required

class ReviewView(View):
    @login_required
    def post(self,request,product_id):
        try:
            data = json.loads(request.body)

            user      = request.user
            comment   = data['comment']
            rating    = data['rating']
            image_url = data['image_url']

            if not product_id or not Product.objects.filter(id=product_id).exists():
                return JsonResponse({"message": "PRODUCT_NOT_EXIST"},status=404)

            review = Review.objects.create(
                    user_id    = user.id,
                    comment    = comment,
                    rating     = rating,
                    product_id = product_id
                   )

            for image in image_url:
                ReviewPhoto.objects.create(
                    image_url = image,
                    review_id = review.id
                )

            return JsonResponse({"message":"REVIEW_POSTED"},status=201)

        except Product.DoesNotExist:
            return JsonResponse({'message':'PRODUCT_NOT_EXIST'}, status=404)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)

    def get(self,request,product_id):
        try:
            product = Product.objects.get(id=product_id)
            data = [{
               'user'     : review.user.name,
               'image_url': [image.image_url for image in review.reviewphoto_set.all()],
               'comment'  : review.comment,
               'rating'   : review.rating,
           } for review in product.review_set.all()]

            return JsonResponse({'data':data}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message':'PRODUCT_NOT_EXISTS'},status=404)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

    @login_required
    def delete(self,request,review_id):
        user = request.user

        if not review_id or not Review.objects.filter(id=review_id).exists():
            return JsonResponse({"message":"REVIEW_NOT_EXIST"},status=404)

        if not Review.objects.filter(id=review_id,user_id=user.id).exists():
            return JsonResponse({"message":"USER_NOT_AUTHORIZED"},status=401)

        Review.objects.get(id=review_id,user_id=user.id).delete()
        return JsonResponse({"message":"REVIEW_DELETED"},status=201)


