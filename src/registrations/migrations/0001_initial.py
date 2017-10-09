# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=10)),
                ('thana', models.CharField(max_length=120)),
                ('district', models.CharField(max_length=120)),
                ('division', models.CharField(max_length=120)),
                ('mate', models.CharField(max_length=10)),
                ('spous', models.CharField(max_length=10)),
                ('kids', models.CharField(max_length=10)),
                ('guests', models.CharField(max_length=10)),
                ('others', models.CharField(max_length=10)),
                ('total', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.CharField(max_length=30)),
                ('payableamount', models.CharField(max_length=200)),
                ('paidamount', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=10)),
                ('details', models.CharField(max_length=120)),
                ('remarks', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('registrationaddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.RegistrationAddress')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('spousname', models.CharField(blank=True, max_length=120, null=True)),
                ('gender', models.CharField(max_length=120)),
                ('kids', models.CharField(blank=True, max_length=120, null=True)),
                ('mobilenumber', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('bloodgroup', models.CharField(blank=True, max_length=120, null=True)),
                ('profession', models.CharField(blank=True, max_length=120, null=True)),
                ('organization', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='registrationaddress',
            name='registrationpersonal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.RegistrationPersonal'),
        ),
    ]
