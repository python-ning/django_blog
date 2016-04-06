from django.shortcuts import render
from models import *


def index(request):
    banners = Banner.objects.all()
    articles = Article.objects.all()[:4]
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    data = {'banners': banners,
            'articles': articles,
            'categorys': categorys,
            'tags': tags
            }
    return render(request, 'index.html', data)


def photo(request):
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    photos = Photo.objects.order_by('create_date')[:16]
    data = {
        'categorys': categorys,
        'tags': tags,
        'photos': photos
    }
    return render(request, 'photo.html', data)


def article(request):
    articles = Article.objects.all()
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    data = {'articles': articles,
            'categorys': categorys,
            'tags': tags,
            'new_articles': new_articles
            }
    return render(request, 'article.html', data)


def contact(request):
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    data = {
        'categorys': categorys,
        'tags': tags
    }
    return render(request, 'contact.html', data)


def article_info(request, id):
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    new_articles = Article.objects.order_by('create_date')
    articleinfo = Article.objects.filter(id=id)[0]
    data = {'articleinfo': articleinfo,
            'new_articles': new_articles,
            'categorys': categorys,
            'tags': tags
            }
    return render(request, 'article_info.html', data)


def category_info(request, id):
    categoryinfo = Category.objects.filter(id=id)[0]
    article_categorys = Article.objects.filter(category_id=id)
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    data = {
        'categoryinfo': categoryinfo,
        'article_categorys': article_categorys,
        'new_articles': new_articles,
        'categorys': categorys,
        'tags': tags
    }
    return render(request, 'category_info.html', data)


def tag_info(request, id):
    taginfo = Tag.objects.filter(id=id)[0]
    article_tags = Article.objects.filter(tag_id=id)
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    data = {
        'taginfo': taginfo,
        'article_tags': article_tags,
        'new_articles': new_articles,
        'categorys': categorys,
        'tags': tags
    }
    return render(request, 'tag_info.html', data)
