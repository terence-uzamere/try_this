# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_suggestion_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='category',
            field=models.IntegerField(default=0, choices=[(0, b'Select...'), (1, b'Night Life'), (2, b'Restaurants'), (3, b'TV Shows/Movies'), (4, b'Recipes'), (5, b'Food'), (6, b'Lifestyle')]),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='category',
            field=models.IntegerField(default=0, choices=[(0, b'Select...'), (1, b'Night Life'), (2, b'Restaurants'), (3, b'TV Shows/Movies'), (4, b'Recipes'), (5, b'Food'), (6, b'Lifestyle')]),
        ),
    ]
