# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_books', '0006_auto_20180519_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_book',
            name='kind',
            field=models.CharField(default=b'\xe5\x85\xb6\xe4\xbb\x96\xe4\xb9\xa6\xe7\xb1\x8d', max_length=20, choices=[(b'\xe7\xa7\x91\xe5\xb9\xbb\xe4\xbd\x9c\xe5\x93\x81', 1), (b'\xe7\xa7\x91\xe6\x99\xae\xe4\xb9\xa6\xe7\xb1\x8d', 2), (b'\xe6\x96\x87\xe5\x8c\x96\xe8\x89\xba\xe6\x9c\xaf', 3), (b'\xe5\x85\xb6\xe4\xbb\x96\xe4\xb9\xa6\xe7\xb1\x8d', 4)]),
        ),
    ]
