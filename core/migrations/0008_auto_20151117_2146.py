# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151117_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='visibility',
            new_name='category',
        ),
    ]
