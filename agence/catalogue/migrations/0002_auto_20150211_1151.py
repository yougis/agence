# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='resume',
            field=models.CharField(max_length=2000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='workshop_price',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='workshop_term',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='age',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='duration',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='full_nb_people',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='full_price',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='light_nb_people',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='light_price',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='synops',
            field=models.CharField(max_length=2000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='teazer_url',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scene',
            name='title',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
