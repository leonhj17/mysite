# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2017-05-02 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], max_length=6)),
            ],
            options={
                'verbose_name': '\u4e2a\u4eba\u4fe1\u606f',
                'verbose_name_plural': '\u4e2a\u4eba\u4fe1\u606f',
            },
        ),
    ]
