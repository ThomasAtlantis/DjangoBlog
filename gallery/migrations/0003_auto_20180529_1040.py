# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180529_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='original',
            field=easy_thumbnails.fields.ThumbnailerImageField(default=b'./photos/none.jpg', upload_to=b'./photos'),
        ),
    ]
