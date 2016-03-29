# coding:utf-8
from django.db import models

# Create your models here.


class Nav(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    pid = models.IntegerField(verbose_name='pid')
    types = models.BooleanField(verbose_name='类型')
    status = models.BooleanField(verbose_name='状态')
    order = models.IntegerField(verbose_name='排序')
    banner = models.ImageField(verbose_name='导航图')

    class Meta:
        verbose_name = '导航'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    types = models.BooleanField(verbose_name='类型')
    status = models.BooleanField(verbose_name='状态')
    navid = models.IntegerField(verbose_name='导航对应ｉｄ')
    description = models.CharField(max_length=150, verbose_name='描述')
    date = models.DateField(verbose_name='日期')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=30, verbose_name='图片名称')
    dirs = models.CharField(max_length=100, verbose_name='图片路径')
    status = models.BooleanField(verbose_name='状态')
    navid = models.IntegerField(verbose_name='导航对应ｉｄ')

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name
