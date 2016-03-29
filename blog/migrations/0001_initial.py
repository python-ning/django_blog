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
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('types', models.BooleanField()),
                ('status', models.BooleanField()),
                ('navid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('dirs', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('navid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa')),
                ('pid', models.IntegerField()),
                ('types', models.BooleanField()),
                ('status', models.BooleanField()),
                ('order', models.IntegerField()),
                ('banner', models.ImageField(upload_to=b'')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u5bfc\u822a',
                'verbose_name_plural': '\u5bfc\u822a',
            },
        ),
    ]
