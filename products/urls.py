from django.urls import path
from .views      import MainView,AreaView,RoomDetailView,ProductsDetailView

urlpatterns =[
    path('/main',MainView.as_view()),
    path('/area/<int:area_id>',AreaView.as_view()),
    path('/room/<int:room_id>',RoomDetailView.as_view()),
    path('/goods/<int:product_id>',ProductsDetailView.as_view())

]