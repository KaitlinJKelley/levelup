# Generated by Django 3.2.1 on 2021-05-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0007_alter_event_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='gamer',
            new_name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_address',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default='12:00'),
        ),
    ]
