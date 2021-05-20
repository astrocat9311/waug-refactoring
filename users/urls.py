from django.urls import path
from users.views import UserSignupView, UserLoginView,WishlistView,KakaoLoginView,KakaoLoginCallbackView

urlpatterns = [
    path('/signup',UserSignupView.as_view()),
    path('/login', UserLoginView.as_view()),
    path('/wishlist',WishlistView.as_view()),
    path('/kakao/login',KakaoLoginView.as_view()),
    path('/kakao/login/callback',KakaoLoginCallbackView.as_view())
]
