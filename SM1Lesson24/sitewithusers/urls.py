from django.urls import path, include
from sitewithusers.views import MainPageView, RegistrationPageView, CheckPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('sing-up/', RegistrationPageView.as_view(), name='registrationpage'),
    path('sing-in/', CheckPageView.as_view(), name='checkpage')
]
