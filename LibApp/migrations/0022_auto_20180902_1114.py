# Generated by Django 2.0.8 on 2018-09-02 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0021_auto_20180902_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(default=datetime.date(2018, 9, 2)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='returned_date',
            field=models.DateField(default=datetime.date(2018, 10, 2)),
        ),
    ]
