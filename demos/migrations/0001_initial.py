# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('icon', models.ImageField(default=b'./photos/none.jpg', upload_to=b'./photos')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
