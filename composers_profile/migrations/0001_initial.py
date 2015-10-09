# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComposersProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=b'100')),
                ('last_name', models.CharField(max_length=b'100')),
                ('gender', models.CharField(max_length=b'1', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.CharField(max_length=b'100')),
                ('latitude', models.FloatField(max_length=b'100')),
                ('longitude', models.FloatField(max_length=b'100')),
                ('current', models.CharField(max_length=b'100')),
                ('past', models.CharField(max_length=b'100')),
                ('education', models.CharField(max_length=b'100')),
                ('summary', models.CharField(max_length=b'100')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
