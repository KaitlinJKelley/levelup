# Generated by Django 3.2 on 2021-05-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_rename_organizer_event_gamer'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(default='me', max_length=100),
            preserve_default=False,
        ),
    ]