# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180913_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='editor_type',
            field=models.BooleanField(default=True),
        ),
    ]
