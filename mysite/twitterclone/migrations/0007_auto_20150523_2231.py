# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0006_auto_20150523_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
