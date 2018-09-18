# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180913_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85\xe5\x90\x8d\xe5\xad\x97')),
                ('body', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('article', models.ForeignKey(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x89\x80\xe5\xb1\x9e\xe6\x96\x87\xe7\xab\xa0', to='articles.Article')),
            ],
        ),
    ]
