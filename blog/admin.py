# coding:utf-8
from django.contrib import admin
from models import Nav, Photo, Article, Banner, Category, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'create_date', 'update_date')


admin.site.register(Nav)
admin.site.register(Photo)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Tag)
