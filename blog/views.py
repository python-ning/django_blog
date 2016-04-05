from django.shortcuts import render
from models import *

def index(request):
    banners = Banner.objects.all()
    return render(request, 'index.html', {'banners': banners})


def photo(request): 
    return render(request, 'photo.html', locals())


def article(request):
    return render(request, 'article.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())

def article_info(request):
    return render(request, 'article_info.html', locals())
