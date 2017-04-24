# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-21 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feature_text',
            field=models.TextField(default='Featured Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='feature_title',
            field=models.TextField(default='Featured Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='profile_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='profile_text',
            field=models.TextField(default='Profile Desription'),
            preserve_default=False,
        ),
    ]