from django.contrib import admin
from .models import Auto,Automodel, Brand, UserCar

# Register your models here.
admin.site.register(Auto)
admin.site.register(Automodel)
admin.site.register(Brand)
admin.site.register(UserCar)