# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='e_book',
            old_name='discription',
            new_name='description',
        ),
    ]
