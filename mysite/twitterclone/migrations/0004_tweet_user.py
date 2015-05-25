# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterclone', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default=1, editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
