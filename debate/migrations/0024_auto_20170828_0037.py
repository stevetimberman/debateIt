# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0023_auto_20170828_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debatetopic',
            old_name='cover_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='debatetopic',
            old_name='topic_tags',
            new_name='tags',
        ),
    ]