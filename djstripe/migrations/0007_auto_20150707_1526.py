# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0006_auto_20150706_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='currency',
            field=models.CharField(max_length=10, choices=[(b'gbp', 'Pounds \xa3'), (b'usd', b'U.S.D $')]),
        ),
    ]
