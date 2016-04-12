# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField  # 富文本编辑器
# Create your models here.

# 导航表


class Nav(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    pid = models.IntegerField(verbose_name='pid')
    types = models.BooleanField(verbose_name='类型')
    status = models.BooleanField(verbose_name='状态')
    order = models.IntegerField(verbose_name='排序')
    banner = models.ImageField(upload_to='banner', verbose_name='导航图')

    class Meta:
        verbose_name = '导航'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name

# 分类表


class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name='分类名')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
# 标签表


class Tag(models.Model):
    name = models.CharField(max_length=15, verbose_name='标签名')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# 文章表


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='文章标题')
    types = models.BooleanField(verbose_name='文章类型')
    status = models.BooleanField(verbose_name='文章状态')
    description = models.CharField(max_length=150, verbose_name='文章描述')
    create_date = models.DateField(verbose_name='文章创建日期')
    update_date = models.DateField(verbose_name='文章更新日期')
    article_image = models.ImageField(
        upload_to='article_image', verbose_name="文章图片")
    # models.TextField(verbose_name='正文')
    content = RichTextField(verbose_name='内容')
    category = models.ForeignKey(Category, verbose_name='分类')
    tag = models.ForeignKey(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.title

# 相册表


class Photo(models.Model):
    image = models.ImageField(upload_to='photo', verbose_name='相册图片')
    create_date = models.DateField(verbose_name='创建时间')
    name = models.CharField(max_length=30, verbose_name="相册图片名字")

    class Meta:
        verbose_name = '相册图片'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name

# Banner表


class Banner(models.Model):
    image = models.ImageField(upload_to='banner', verbose_name='Banner图片')
    name = models.CharField(max_length=30, verbose_name="Banner名字")

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name
