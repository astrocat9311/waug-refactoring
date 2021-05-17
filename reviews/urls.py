from django.urls import path
from .views      import ReviewListView,ReviewPostView

urlpatterns =[
    path('',ReviewPostView.as_view()),
    path('/product/<int:product_id>',ReviewListView.as_view()),
]