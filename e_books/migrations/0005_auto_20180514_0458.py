# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_books', '0004_auto_20180514_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_book',
            name='description',
            field=models.TextField(default=b''),
        ),
    ]
