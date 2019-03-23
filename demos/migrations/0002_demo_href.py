# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='href',
            field=models.CharField(default=b'#', max_length=100),
        ),
    ]
