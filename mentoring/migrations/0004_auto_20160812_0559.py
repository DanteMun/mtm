# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0003_auto_20160810_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_by_mentor',
            name='date',
            field=models.DateTimeField(default='yyyy-mm-dd 형식으로 써주세요.', verbose_name='멘토링 날짜'),
        ),
    ]
