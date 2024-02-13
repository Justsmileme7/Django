from django.urls import path, re_path
from .views import MainPageView, NewsPageView
from .registration import SignUpView, SignInView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('/news/<int:id>/', NewsPageView.as_view(), name='newspage'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),

]