import datetime

from django.shortcuts import render
from django.views import View
from sitewithusers.models import ListUsers
from django.http.response import HttpResponse


# Create your views here.

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        count = ListUsers.objects.count()
        list_of_users = ListUsers.objects.filter(pk__gte=count - 10)
        list_of_hidden_users = []
        for user in list_of_users:
            before_at, after_at = user.e_mail.split('@')
            hidden_part = '*' * (len(before_at) - 2)
            list_of_hidden_users.append(f'{before_at[:2]}{hidden_part}@{after_at}')

        return render(request, 'mainpage.html', context={'count': count, 'users': list_of_hidden_users})


class RegistrationPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registrationpage.html')

    def post (self, request, *args, **kwargs):
        mail = request.POST.get('e-mail')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeatpassword')
        #now = datetime.datetime.now()
        user = ListUsers(e_mail=mail, password=password)
        user.save()
        print(mail, password, repeat_password)
        return render(request, 'registrationpage.html')


class CheckPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'checkpage.html')
