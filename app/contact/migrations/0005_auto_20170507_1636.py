# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-07 21:36
from __future__ import unicode_literals

import contact.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20170507_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=contact.fields.ModelPhoneField(max_length=10, verbose_name='Phone Number'),
        ),
    ]