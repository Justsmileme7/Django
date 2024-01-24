from django.urls import path, include
from sitewithusers.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage')
]
