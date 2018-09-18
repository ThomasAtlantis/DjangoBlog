# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_books', '0002_auto_20180514_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='e_book',
            name='fileName',
            field=models.SlugField(unique=True, default=2),
            preserve_default=False,
        ),
    ]
