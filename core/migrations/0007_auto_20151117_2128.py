# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151117_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='comments',
            field=models.ForeignKey(blank=True, to='core.Comments', null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='suggestion',
            field=models.ForeignKey(blank=True, to='core.Suggestion', null=True),
        ),
    ]
