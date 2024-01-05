from django.db import models

from article.models import Article


# Create your models here.
class Comment(models.Model):
    commit_content = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=100)
    e_mail = models.EmailField()
    commit_date = models.DateTimeField
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
