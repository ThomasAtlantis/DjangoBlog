# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_books', '0003_e_book_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_book',
            name='fileName',
            field=models.FileField(default=b'', upload_to=b'./e_books/'),
        ),
    ]
