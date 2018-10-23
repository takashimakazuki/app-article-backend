from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
    article_id = models.IntegerField('ID')
    article_title = models.CharField('タイトル', max_length=100)
    article_content = models.CharField('内容',max_length=2000)
    article_author = models.CharField('投稿者', max_length=50)
    article_created = models.DateTimeField('投稿日')

    def __str__(self):
        return self.article_title

    def was_created_recentry(self):
        return self.article_created >= timezone.now() - datetime.timedelta(days=1)
