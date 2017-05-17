# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-07 20:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, message='U.S. phone numbers consist of exactly 10 digits.'), django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z', 32), code='invalid', message='Enter a valid phone number (Only Integers).')], verbose_name='Phone Number'),
        ),
    ]