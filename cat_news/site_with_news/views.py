from django.shortcuts import render
from django.views import View
from .models import News


# Create your views here.
class MainPageView(View):
    PAGE_TITLE = 'Cats news'

    def get(self, request, *args, **kwargs):
        sort_by = request.GET.get('sort', 'date_of_create')  # получаем из нтмл переменную sort
        order_by = request.GET.get('order', 'back_order')
        sort_by = sort_by if order_by == 'wright_order' else f'-{sort_by}'
        news = News.objects.order_by(sort_by)  # достаем отсортированные  объекты из базы данных из таблицы news
        for new in news:
            list_of_news = new.context.split(' ')[:10]
            description = ' '.join(list_of_news)
            new.context = description
        return render(request, 'mainpage.html',
                      context={"title": self.PAGE_TITLE,
                               'news_list': news,
                               })


class NewsPageView(View):

    def get(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)  # достаем одну новость по ИД из базы данных из таблицы news
        title = news.title
        return render(request, 'newspage.html',
                      context={"title": title,
                               'news': news,
                               })


''' 
DEFAULT_NEWS_PICTURE = 'media/default.jpg'

    def get(self, request, *args, **kwargs):
        sort_by = request.GET.get('sort', 'pub_date')
        order_by = request.GET.get('order', 'desc')
        sort_by = sort_by if order_by == 'asc' else f'-{sort_by}'
        news = News.objects.order_by(sort_by)[:20]
        for new in news:
            desc_worlds_list = new.body.split(' ')[:10]
            description = ' '.join(desc_worlds_list)
            new.body = description

        return render(request, 'index.html',
                      context={'sort': sort_by, 'news_list': news, 'title': self.TITLE,
                               'default_jpg': self.DEFAULT_NEWS_PICTURE})
'''
