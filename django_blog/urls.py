from django.conf.urls import include, url, patterns
from django.contrib import admin
import settings
from blog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', photo.views.main, name='index'),
    url(r'^$', index, name='index'),
    url(r'^photo$', photo, name='photo'),
    url(r'^article$', article, name='article'),
    url(r'^contact$', contact, name='contact'),
    url(r'^article_info$', article_info, name='article_info'),
]

urlpatterns += patterns('',
    url(r'^uploads/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.BASE_DIR}),
)