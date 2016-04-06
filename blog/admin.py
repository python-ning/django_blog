# coding:utf-8
from django.contrib import admin
from models import Nav, Photo, Article, Banner, Category, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'create_date', 'update_date')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'create_date', 'image')


admin.site.register(Nav)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Tag)
