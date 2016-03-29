from django.shortcuts import render


def index(request):
    return render(request, 'index.html', locals())


def photo(request):
    return render(request, 'photo.html', locals())


def article(request):
    return render(request, 'article.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())
