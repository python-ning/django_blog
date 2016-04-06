# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('types', models.BooleanField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('status', models.BooleanField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x8a\xb6\xe6\x80\x81')),
                ('description', models.CharField(max_length=150, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('create_date', models.DateField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('update_date', models.DateField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x9c\x9f')),
                ('article_image', models.ImageField(upload_to=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x9b\xbe\xe7\x89\x87')),
                ('content', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'Banner\xe5\x9b\xbe\xe7\x89\x87')),
                ('name', models.CharField(max_length=30, verbose_name=b'Banner\xe5\x90\x8d\xe5\xad\x97')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pid', models.IntegerField(verbose_name=b'pid')),
                ('types', models.BooleanField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('status', models.BooleanField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('order', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('banner', models.ImageField(upload_to=b'', verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\x9b\xbe')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u5bfc\u822a',
                'verbose_name_plural': '\u5bfc\u822a',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\x9b\xbe\xe7\x89\x87')),
                ('create_date', models.DateField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\x90\x8d\xe5\xad\x97')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u76f8\u518c',
                'verbose_name_plural': '\u76f8\u518c',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe', to='blog.Tag'),
        ),
    ]
