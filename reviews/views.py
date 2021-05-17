import json

from django.http     import JsonResponse
from django.views    import View
from .models         import Review,ReviewPhoto
from products.models import Product
from utils           import login_required
from json            import JSONDecodeError

class ReviewPostView(View):
    @login_required
    def post(self,request):
        try:
            data    = json.loads(request.body)
            user    = request.user
            print(user.id)
            product = Product.objects.get(id=data['product_id'])

            review = Review.objects.create(
                    user    = user,
                    comment = data['comment'],
                    rating  = data['rating'],
                    product = product
                   )

            for image in data['image_url']:
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

class ReviewListView(View):
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