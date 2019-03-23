# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_editor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='Category.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='editor_type',
            field=models.BooleanField(default=True, verbose_name=b'\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8MarkDown'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='tag_articles', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe', to='Tag.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
    ]
