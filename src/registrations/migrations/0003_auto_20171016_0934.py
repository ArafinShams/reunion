# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20171015_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationaddress',
            name='note',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrationpayment',
            name='details',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationpayment',
            name='paidamount',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registrationpayment',
            name='remarks',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
