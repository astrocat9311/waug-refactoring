import json

from django.views import View
from .models      import (Category,Area,City,District,RoomType,
                          Room,ServiceCategory,Service,RoomImage,
                          ProductType,Product,ProductImage,ProductOption)
from django.http  import JsonResponse

class MainView(View):
    def get(self,request):

       category_data = [{
           'name'     : category.name,
           'image_url': category.image_url
       } for category in Category.objects.all()]

       area_data = [{
           'name': area.name,
           'image_url': area.image_url
       } for area in Area.objects.all()]

       data = {
           'category_list': category_data,
           'area_list': area_data
       }

       return JsonResponse(json.dumps(data),status=200)

class AreaView(View):
    def get(self,request,area_id):
        area     = Area.objects.get(id=area_id)
        rooms    = Area.room_set.all()
        products = Area.product_set.all()


        return JsonResponse({'data':data},status=200)

class RoomDetailView(View):
    def get(self,request,room_id):
        room = Room.objects.get(id=room_id)

        data = {
                 'name': room.name,
                 'rating': room.rating,
                 'grade': room.grade,
                 'description': room.description,
                 'address': room.address,
                 'latitude': room.latitude,
                 'longitude': room.longitude,
                 'category': room.category.name,
                 'area': room.area.name,
                 'city': room.city.name,
                 'district': room.district.name,
                 'price':room.price,
                 'image_url': [image.image_url for image in room.roomimage_set.all()],
                 'type':room.type.name
        }

        return JsonResponse({'data':data}, status=200)

class ProductsDetailView(View):
    def get(self,request,product_id):
        product = Product.objects.get(id=product_id)

        data = {
            'name': product.name,
            'rating': product.rating,
            'description': product.description,
            'address': product.address,
            'latitude': product.latitude,
            'longitude': product.longitude,
            'category': product.category.name,
            'area': product.area.name,
            'city': product.city.name,
            'district': product.district.name,
            'price': product.price,
            'type': product.type.name
        }

        return JsonResponse({'data':data},status=200)



















