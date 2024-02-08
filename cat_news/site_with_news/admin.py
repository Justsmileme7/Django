from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe

from site_with_news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'context', 'rating')
    search_fields = ('title', 'context')
    ordering = ('title', 'rating')

    def preview(self, instance: News):
        if instance.image:
            return mark_safe(f'<img style="max-width: 200px" src="{instance.image.url}" alt="">')
        return mark_safe('Without picture')

