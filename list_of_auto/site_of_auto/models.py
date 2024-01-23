from django.db import models


# Create your models here.
class Auto(models.Model):
    CHOiCES = [
        ('FR', 'FREE'),
        ('USE', 'INUSE')
    ]
    status = models.CharField(max_length=255, choices=CHOiCES)
    autobrand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    automodel = models.ForeignKey('Automodel', on_delete=models.CASCADE)
    vin_code = models.CharField(max_length=255)
    user = models.ForeignKey('UserCar', on_delete=models.CASCADE)


class Automodel(models.Model):
    automodel = models.CharField(max_length=255)
    autobrand = models.ForeignKey('Brand', on_delete=models.CASCADE)




class Brand(models.Model):
    name = models.CharField(max_length=255)
    image_brand = models.ImageField()


class UserCar(models.Model):
    username = models.CharField(max_length=255)
    user_mail = models.EmailField()
    user_phone_number = models.CharField(max_length=12)








