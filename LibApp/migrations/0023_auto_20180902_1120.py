# Generated by Django 2.0.8 on 2018-09-02 05:50

import LibApp.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0022_auto_20180902_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='returned_date',
            field=models.DateField(default=LibApp.models.get_deadline),
        ),
    ]
