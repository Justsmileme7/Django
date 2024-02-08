from django.shortcuts import render
from django.views import View


# Create your views here.
class MainPageView(View):
    PAGE_TITLE = 'Cats news'
    news = []

    def get(self, request, *args, **kwargs):
        return render(request, 'mainpage.html', context={"title": self.PAGE_TITLE})


        '''def preview(self, instance: Brand):
        if instance.image_brand:
            return mark_safe(f'<img style="max-width: 75px" src="{instance.image_brand.url}" alt="">')
        return mark_safe('Without logo')'''