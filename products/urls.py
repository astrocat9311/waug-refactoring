from django.urls import path
from .views import RoomDetailView,ProductsDetailView

urlpatterns =[

    path('/room/<int:room_id>',RoomDetailView.as_view()),
    path('/goods/<int:product_id>',ProductsDetailView.as_view())

]