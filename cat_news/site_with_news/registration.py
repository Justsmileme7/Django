from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import News


# Create your views here.
class SignUpView(View):
    @staticmethod
    def get(request):
        return render(request, 'sign_up.html')

    @staticmethod
    def post(request):
        username, password = request.POST['username'], request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('sign_in')


class SignInView(View):
    @staticmethod
    def get(request):
        return render(request, 'sign_in.html')

    @staticmethod
    def post(request):
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('profile')

        return redirect('sign_in')

