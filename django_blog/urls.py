from django.conf.urls import include, url, patterns
from django.contrib import admin
import settings
from blog.views import *

urlpatterns = [
    url(r'^article_info/(?P<id>\d+)$', article_info, name='article_info'),
    url(r'^category_info/(?P<id>\d+)$', category_info, name='category_info'),
    url(r'^date_info/(?P<year>\d+)/(?P<month>\d+)$', date_info, name='date_info'),
    url(r'^tag_info/(?P<id>\d+)$', tag_info, name='tag_info'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^photo$', photo, name='photo'),
    url(r'^article$', article, name='article'),
    url(r'^contact$', contact, name='contact'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
]

# urlpatterns += patterns('',
#     url(r'^uploads/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.BASE_DIR}),
# )