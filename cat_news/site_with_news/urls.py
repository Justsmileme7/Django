from django.urls import path, re_path
from .views import MainPageView, NewsPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('/news/<int:id>/', NewsPageView.as_view(), name='newspage'),

]