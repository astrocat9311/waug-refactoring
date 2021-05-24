from django.urls import path
from .views      import CategoryView,AreaView,RoomDetailView,ProductsDetailView,AreaWeatherView,ProductView,RoomView

urlpatterns =[
    path('/category',CategoryView.as_view()),
    path('/area',AreaView.as_view()),
    path('/area/<int:area_id>/products',ProductView.as_view()),
    path('/area/<int:area_id>/rooms',RoomView.as_view()),
    path('/area/<str:area_name>/weather',AreaWeatherView.as_view()),
    path('/room/<int:room_id>',RoomDetailView.as_view()),
    path('/goods/<int:product_id>',ProductsDetailView.as_view()),
]

