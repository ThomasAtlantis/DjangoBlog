# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180529_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='original',
            field=django_thumbs.db.models.ImageWithThumbsField(default=b'./photos/none.jpg', upload_to=b'./photos'),
        ),
    ]
