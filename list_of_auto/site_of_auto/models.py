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


class Automodel(models.Model):
    automodel = models.CharField(max_length=255)
    autobrand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.automodel


class Brand(models.Model):
    name = models.CharField(max_length=255)
    image_brand = models.ImageField(null=True, blank=True, default=None, upload_to='logos')

    def __str__(self):
        return self.name


class UserCar(models.Model):
    username = models.CharField(max_length=255)
    user_mail = models.EmailField()
    user_phone_number = models.CharField(max_length=12)
    auto = models.OneToOneField('Auto', on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.username
