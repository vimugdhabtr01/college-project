# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('composers_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='composersprofile',
            old_name='current',
            new_name='current_song',
        ),
        migrations.RenameField(
            model_name='composersprofile',
            old_name='past',
            new_name='hit_songs',
        ),
    ]
