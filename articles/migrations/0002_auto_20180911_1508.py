# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.AlterField(
            model_name='article',
            name='kind',
            field=models.ForeignKey(to='Category.Category'),
        ),
    ]
