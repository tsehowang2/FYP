# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-17 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200417_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_food',
            field=models.ManyToManyField(blank=True, default=None, through='order.Order_State', to='restaurant.Food'),
        ),
        migrations.AlterField(
            model_name='order_state',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Food'),
        ),
        migrations.AlterField(
            model_name='order_state',
            name='state',
            field=models.CharField(choices=[('ordered', 'ordered'), ('making', 'making'), ('finished', 'finished'), ('served', 'served'), ('cancelled', 'cancelled')], default='ordered', max_length=10),
        ),
    ]