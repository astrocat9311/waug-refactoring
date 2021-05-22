from django.urls import path
from .views      import ReviewListView,ReviewPostView

urlpatterns =[
    path('',ReviewPostView.as_view()),
    path('/product/<int:product_id>/review',ReviewListView.as_view()),
]