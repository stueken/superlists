# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0006_list_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_with', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(null=True, related_name='owner', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
