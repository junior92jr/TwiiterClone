# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0011_auto_20150523_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user',
        ),
    ]
