# Generated by Django 3.2.1 on 2021-05-06 15:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0005_alter_event_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 35, 41, 37324, tzinfo=utc)),
        ),
    ]
