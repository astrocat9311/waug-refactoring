from django.urls import path
from users.views import UserSignupView, UserLoginView,WishlistView

urlpatterns = [
    path('/signup',UserSignupView.as_view()),
    path('/login', UserLoginView.as_view()),
    path('/wishlist',WishlistView.as_view()),
]
