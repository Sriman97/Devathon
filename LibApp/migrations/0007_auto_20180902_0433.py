# Generated by Django 2.0.8 on 2018-09-01 23:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0006_auto_20180902_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 1, 23, 3, 26, 845884, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='returned_date',
            field=models.DateField(),
        ),
    ]
