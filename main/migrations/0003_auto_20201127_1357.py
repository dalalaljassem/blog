# Generated by Django 2.2 on 2020-11-27 13:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201127_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 13, 57, 2, 624824, tzinfo=utc)),
        ),
    ]
