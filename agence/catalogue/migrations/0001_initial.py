# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0006_auto_20141028_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('resume', models.CharField(max_length=2000, null=True, blank=True)),
                ('workshop_price', models.IntegerField(null=True, blank=True)),
                ('workshop_term', models.CharField(max_length=200, null=True, blank=True)),
                ('logo', models.ForeignKey(blank=True, to='photologue.Photo', null=True)),
                ('photo_gallery', models.ForeignKey(blank=True, to='photologue.Gallery', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hour', models.IntegerField(null=True, blank=True)),
                ('minute', models.IntegerField(null=True, blank=True)),
                ('condition', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ForeignKey(blank=True, to='photologue.Photo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('synops', models.CharField(max_length=2000, null=True, blank=True)),
                ('interpret', models.CharField(max_length=500, null=True, blank=True)),
                ('full_price', models.IntegerField(null=True, blank=True)),
                ('full_nb_people', models.IntegerField(null=True, blank=True)),
                ('light_price', models.IntegerField(null=True, blank=True)),
                ('light_nb_people', models.IntegerField(null=True, blank=True)),
                ('teazer_url', models.CharField(max_length=200, null=True, blank=True)),
                ('disponibility', models.CharField(max_length=200, null=True, blank=True)),
                ('dossier_presse', models.FileField(null=True, upload_to=b'dossiers_presse/', blank=True)),
                ('dossier_peda', models.FileField(null=True, upload_to=b'dossiers_peda/', blank=True)),
                ('archive_zip', models.FileField(null=True, upload_to=b'archives_zip/', blank=True)),
                ('age', models.ForeignKey(blank=True, to='catalogue.Age', null=True)),
                ('company', models.ForeignKey(to='catalogue.Company')),
                ('duration', models.ForeignKey(blank=True, to='catalogue.Duration', null=True)),
                ('photo_gallery', models.ForeignKey(blank=True, to='photologue.Gallery', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SceneCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_cat',
            field=models.ManyToManyField(to='catalogue.SceneCat', null=True, blank=True),
            preserve_default=True,
        ),
    ]
