# Generated by Django 2.2 on 2020-11-28 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201128_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 14, 28, 14, 205960, tzinfo=utc)),
        ),
    ]
