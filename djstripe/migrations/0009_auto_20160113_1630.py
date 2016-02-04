# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_auto_20150714_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentsubscription',
            name='plan',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='plan',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
