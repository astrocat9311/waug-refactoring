from django.urls import path
from users.views import UserSignupView, UserLoginView, CouponView

urlpatterns = [
    path('/signup',UserSignupView.as_view()),
    path('/login', UserLoginView.as_view()),
    path('/coupon',CouponView.as_view()),
]
