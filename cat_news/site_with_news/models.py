from django.db import models


# Create your models here.

class News(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50, unique=True)
    context = models.TextField()
    rating = models.IntegerField(default=0)
    rating_popular = models.IntegerField(default=0)
    date_of_create = models.DateTimeField()
    author = models.CharField(max_length=20)


class Comment(models.Model):
    nickname = models.CharField(max_length=10)
    context_of_comment = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    date_of_create_comment = models.DateTimeField()
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE)
