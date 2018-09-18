# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('kind', models.CharField(default=b'\xe5\x85\xb6\xe4\xbb\x96\xe7\xb1\xbb\xe5\x9e\x8b', max_length=20, choices=[(b'\xe7\xa7\x91\xe5\xb9\xbb\xe7\x94\xb5\xe5\xbd\xb1', b'\xe7\xa7\x91\xe5\xb9\xbb\xe7\x94\xb5\xe5\xbd\xb1'), (b'\xe9\xad\x94\xe5\xb9\xbb\xe7\x94\xb5\xe5\xbd\xb1', b'\xe9\xad\x94\xe5\xb9\xbb\xe7\x94\xb5\xe5\xbd\xb1'), (b'\xe7\xbe\x8e\xe5\x89\xa7\xe8\x8b\xb1\xe5\x89\xa7', b'\xe7\xbe\x8e\xe5\x89\xa7\xe8\x8b\xb1\xe5\x89\xa7'), (b'\xe5\x85\xb6\xe4\xbb\x96\xe7\xb1\xbb\xe5\x9e\x8b', b'\xe5\x85\xb6\xe4\xbb\x96\xe7\xb1\xbb\xe5\x9e\x8b')])),
                ('video_url', models.CharField(max_length=100)),
                ('introduction_url', models.CharField(max_length=100)),
            ],
        ),
    ]
