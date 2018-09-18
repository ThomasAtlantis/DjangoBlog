# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0002_auto_20180911_1519'),
        ('articles', '0002_auto_20180911_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='kind',
            new_name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='Tag.Tag', blank=True),
        ),
    ]
