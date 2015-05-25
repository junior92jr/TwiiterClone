# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0013_tweet_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='nickname',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
