# Generated by Django 2.0.8 on 2018-09-01 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 2, 0, 47, 1, 121109)),
        ),
    ]