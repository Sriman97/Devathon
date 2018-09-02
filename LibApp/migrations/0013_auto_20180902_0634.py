# Generated by Django 2.0.8 on 2018-09-02 01:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0012_auto_20180902_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 2, 1, 4, 1, 271399, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='returned_date',
            field=models.DateField(default=datetime.datetime(2018, 10, 2, 6, 34, 1, 271399)),
        ),
    ]
