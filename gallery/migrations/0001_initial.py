# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, blank=True)),
                ('original', models.ImageField(default=b'/tmp/none.jpg', upload_to=b'uploads')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
