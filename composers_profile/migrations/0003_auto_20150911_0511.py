# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('composers_profile', '0002_auto_20150910_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotPasswordUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=b'100')),
                ('flag', models.BooleanField(default=False)),
                ('forgotpassworduser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='composersprofile',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='composersprofile',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
