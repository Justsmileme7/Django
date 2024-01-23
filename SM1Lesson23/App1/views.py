from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

class HelloView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html', context={'massage':'Hello', 'color': 'red'})

class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html', context={'massage':'Hello, World', 'color': 'blue'})