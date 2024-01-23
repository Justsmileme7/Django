from django.db import models

# Create your models here.
from django.db import models


class Users(models.Model):
    e_mail = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    user_date = models.DateTimeField

