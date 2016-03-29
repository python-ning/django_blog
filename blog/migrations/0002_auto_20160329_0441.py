# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-id'], 'verbose_name': '\u76f8\u518c', 'verbose_name_plural': '\u76f8\u518c'},
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 3, 29, 4, 41, 22, 640977, tzinfo=utc), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default=1, max_length=150, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='article',
            name='navid',
            field=models.IntegerField(verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\xaf\xb9\xe5\xba\x94\xef\xbd\x89\xef\xbd\x84'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='article',
            name='types',
            field=models.BooleanField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='image',
            name='dirs',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='image',
            name='navid',
            field=models.IntegerField(verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\xaf\xb9\xe5\xba\x94\xef\xbd\x89\xef\xbd\x84'),
        ),
        migrations.AlterField(
            model_name='image',
            name='status',
            field=models.BooleanField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='banner',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='order',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='pid',
            field=models.IntegerField(verbose_name=b'pid'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='status',
            field=models.BooleanField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='types',
            field=models.BooleanField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
