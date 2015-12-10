# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_suggestion_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='rating',
        ),
    ]
