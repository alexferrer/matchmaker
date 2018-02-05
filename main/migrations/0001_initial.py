# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 16:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[(0, 'CLOSE'), (1, 'OPEN')], default=1, max_length=10)),
                ('type_of', models.CharField(choices=[(0, 'BUY'), (1, 'SELL')], default=0, max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]