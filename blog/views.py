from django.shortcuts import render
from models import *


def index(request):
    banners = Banner.objects.all()
    articles = Article.objects.all()[:4]
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', {'banners': banners, 'articles': articles, 'categorys': categorys,
                                          'tags': tags})


def photo(request):
    return render(request, 'photo.html', locals())


def article(request):
    articles = Article.objects.all()
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'article.html', {'articles': articles, 'categorys': categorys, 'tags': tags, 'new_articles': new_articles})


def contact(request):
    return render(request, 'contact.html', locals())


def article_info(request, id):
    return render(request, 'article_info.html', locals())
