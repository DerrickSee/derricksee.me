# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('blog', '0002_auto_20170715_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text=b'1920x1080', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
