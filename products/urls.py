from django.urls import path
from .views      import CategoryView,AreaView,RoomDetailView,ProductsDetailView

urlpatterns =[
    path('/category',CategoryView.as_view()),
    path('/area',AreaView.as_view()),
    path('/room/<int:room_id>',RoomDetailView.as_view()),
    path('/goods/<int:product_id>',ProductsDetailView.as_view()),
]

