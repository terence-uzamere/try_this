# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Night Life'), (1, b'Restaurants'), (2, b'Movies/TV Shows'), (3, b'Recipes'), (4, b'Food'), (5, b'Lifestyle')]),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='name',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='category',
            field=models.IntegerField(default=0, choices=[(0, b'Night Life'), (1, b'Restaurants'), (2, b'Movies/TV Shows'), (3, b'Recipes'), (4, b'Food'), (5, b'Lifestyle')]),
        ),
    ]
