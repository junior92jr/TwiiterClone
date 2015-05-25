# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0014_auto_20150524_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='nickname',
            field=models.ForeignKey(default=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
