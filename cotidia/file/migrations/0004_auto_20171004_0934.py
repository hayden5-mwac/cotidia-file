# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20170908_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('order_id', '-created_at'), 'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
        migrations.AddField(
            model_name='file',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]