# Generated by Django 2.0.8 on 2018-09-01 23:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0007_auto_20180902_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 1, 23, 8, 19, 72517, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='returned_date',
            field=models.DateField(default=datetime.datetime(2018, 10, 2, 4, 38, 19, 72517)),
        ),
    ]
