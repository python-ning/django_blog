# coding:utf-8
from django.contrib import admin
from models import Nav, Image, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')


admin.site.register(Nav)
admin.site.register(Image)
admin.site.register(Article, ArticleAdmin)
