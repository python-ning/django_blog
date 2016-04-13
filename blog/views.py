# coding:utf-8
from django.shortcuts import render
from models import *
from collections import OrderedDict
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # 首页
    banners = Banner.objects.all()
    articles = Article.objects.all()[:4]
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    photos = Photo.objects.all()[:8]
    data = {'banners': banners,
            'articles': articles,
            'categorys': categorys,
            'tags': tags,
            'photos': photos
            }
    return render(request, 'index.html', data)


def photo(request):
    # 相册
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    photos = Photo.objects.order_by('create_date')[:16]
    data = {
        'categorys': categorys,
        'tags': tags,
        'photos': photos
    }
    return render(request, 'photo.html', data)


def article_archives():
    # 公共方法 文章归档
    post_date = Article.objects.dates('create_date', 'month')
    post_date = post_date.reverse()
    post_date_article = []
    for i in range(len(post_date)):
        post_date_article.append([])
    for i in range(len(post_date)):
        curyear = post_date[i].year
        curmonth = post_date[i].month
        tempArticle = Article.objects.filter(
            create_date__year=curyear).filter(create_date__month=curmonth)
        post_date_article[i] = tempArticle
    dicts = OrderedDict()
    for i in range(len(post_date)):
        dicts.setdefault(post_date[i], post_date_article[i])
    return dicts


def article(request):
    # 文章
    LIMIT = 3  # 每页显示的文章数
    articles = Article.objects.all()
    paginator = Paginator(articles, LIMIT)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        topics = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        topics = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        topics = paginator.page(paginator.num_pages)  # 取最后一页的记录
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    dicts = article_archives()

    data = {'articles': articles,
            'categorys': categorys,
            'tags': tags,
            'new_articles': new_articles,
            'dicts': dicts,
            'topics': topics
            }
    return render(request, 'article.html', data)


def article_info(request, id):
    # 文章详情
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    new_articles = Article.objects.order_by('create_date')
    articleinfo = Article.objects.filter(id=id)[0]
    dicts = article_archives()
    data = {'articleinfo': articleinfo,
            'new_articles': new_articles,
            'categorys': categorys,
            'tags': tags,
            'dicts': dicts
            }
    return render(request, 'article_info.html', data)


def category_info(request, id):
    # 分类详情
    categoryinfo = Category.objects.filter(id=id)[0]
    article_categorys = Article.objects.filter(category_id=id)
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    dicts = article_archives()
    data = {
        'categoryinfo': categoryinfo,
        'article_categorys': article_categorys,
        'new_articles': new_articles,
        'categorys': categorys,
        'tags': tags,
        'dicts': dicts
    }
    return render(request, 'category_info.html', data)


def tag_info(request, id):
    # 标签详情
    taginfo = Tag.objects.filter(id=id)[0]
    article_tags = Article.objects.filter(tag_id=id)
    new_articles = Article.objects.order_by('create_date')
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    dicts = article_archives()
    data = {
        'taginfo': taginfo,
        'article_tags': article_tags,
        'new_articles': new_articles,
        'categorys': categorys,
        'tags': tags,
        'dicts': dicts
    }
    return render(request, 'tag_info.html', data)


def date_info(request, year, month):
    # 文章归档详情
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    new_articles = Article.objects.order_by('create_date')
    dicts = article_archives()
    article_date_lists = Article.objects.filter(
        create_date__month=str(month), create_date__year=str(year))
    # only query one for date_info title ↓↓↓
    article_date_month = Article.objects.filter(
        create_date__month=str(month), create_date__year=str(year))[0]
    data = {
        'categorys': categorys,
        'tags': tags,
        'new_articles': new_articles,
        'dicts': dicts,
        'article_date_lists': article_date_lists,
        'article_date_month': article_date_month
    }
    return render(request, 'date_info.html', data)


def contact(request):
    # 联系我
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    data = {
        'categorys': categorys,
        'tags': tags
    }
    return render(request, 'contact.html', data)
