# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151116_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Night Life'), (1, b'Restaurants'), (2, b'TV Shows/Movies'), (3, b'Recipes'), (4, b'Food'), (5, b'Lifestyle')]),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='category',
            field=models.IntegerField(default=0, choices=[(0, b'Night Life'), (1, b'Restaurants'), (2, b'TV Shows/Movies'), (3, b'Recipes'), (4, b'Food'), (5, b'Lifestyle')]),
        ),
    ]
