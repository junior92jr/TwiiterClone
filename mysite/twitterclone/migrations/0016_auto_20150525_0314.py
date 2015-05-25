# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0015_auto_20150524_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tweet',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
