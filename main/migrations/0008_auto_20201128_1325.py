# Generated by Django 2.2 on 2020-11-28 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201127_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 13, 25, 49, 393545, tzinfo=utc)),
        ),
    ]
