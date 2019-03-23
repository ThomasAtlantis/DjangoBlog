# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180911_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='tag_articles', to='Tag.Tag', blank=True),
        ),
    ]
