# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-13 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('postalCode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('person', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='phoneNumbers', to='app.Person')),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='person',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='app.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='app.Person'),
        ),
    ]
