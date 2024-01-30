from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from .models import Auto, Automodel, Brand, UserCar

# Register your models here.

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('autobrand', 'automodel', 'status', 'vin_code')
    list_filter = ('status', 'autobrand')


@admin.register(Automodel)
class AutomodelAdmin(admin.ModelAdmin):
    list_display = ('autobrand', 'automodel')
    list_filter = ('autobrand',)
    search_fields = ('vin_code',)

    def count_auto(self, instance):
        count = Auto.objects.filter(automodel__name=instance.name).count()
        return count

@admin.register(UserCar)
class UserCarAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_mail', 'user_phone_number')
    search_fields = ('user_phone_number',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name')

    def preview(self, instance: Brand):
        if instance.image_brand :
            return mark_safe(f'img scr="{instance.image_brand .url}" alt="">')
        return mark_safe('Without logo')

