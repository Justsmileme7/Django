from django.shortcuts import render
from django.views import View


# Create your views here.
class MainPageView(View):
    PAGE_TITLE = 'Main Page'
    def get(self, request):
        return render(request, 'mainpage.html', context={"title": self.PAGE_TITLE})