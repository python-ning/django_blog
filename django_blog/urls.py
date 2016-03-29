from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^photo$', photo, name='photo'),
    url(r'^article$', article, name='article'),
    url(r'^contact$', contact, name='contact'),
]
