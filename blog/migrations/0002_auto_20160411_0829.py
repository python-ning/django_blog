# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-id'], 'verbose_name': '\u76f8\u518c\u56fe\u7247', 'verbose_name_plural': '\u76f8\u518c\u56fe\u7247'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to=b'article_image', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to=b'banner', verbose_name=b'Banner\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='banner',
            field=models.ImageField(upload_to=b'banner', verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=b'photo', verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\x9b\xbe\xe7\x89\x87\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
