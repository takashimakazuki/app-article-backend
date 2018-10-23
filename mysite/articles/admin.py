from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'article_title', 'article_content', 'article_author',)
    list_display_links = ('article_id', 'article_title')


admin.site.register(Article, ArticleAdmin)
