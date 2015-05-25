# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0007_auto_20150523_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
