# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20150211_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='duration',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
