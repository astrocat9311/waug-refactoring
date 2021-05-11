from django.urls import path
from users.views import UserSignupView, UserLoginView

urlpatterns = [
    path('/signup',UserSignupView.as_view()),
    path('/login', UserLoginView.as_view()),
]
