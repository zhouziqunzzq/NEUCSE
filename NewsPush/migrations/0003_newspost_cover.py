# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPush', '0002_auto_20170605_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='cover',
            field=models.ImageField(default='admin', upload_to='Img'),
            preserve_default=False,
        ),
    ]
