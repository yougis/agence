# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20150211_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='scene_type',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
