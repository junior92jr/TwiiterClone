# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterclone', '0012_remove_tweet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='nickname',
            field=models.ForeignKey(default=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
