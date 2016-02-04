# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0005_charge_captured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='currency',
            field=models.CharField(max_length=10, choices=[(b'gbp', b'Pounds (GBP)'), (b'usd', b'U.S. Dollars')]),
        ),
    ]
