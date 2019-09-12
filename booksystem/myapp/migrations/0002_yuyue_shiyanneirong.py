# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yuyue',
            name='shiyanneirong',
            field=models.CharField(verbose_name='实验内容', max_length=200, blank=True),
        ),
    ]
