# Generated by Django 4.0.3 on 2022-04-10 09:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('entry', '0016_alter_usrinfo_guide_lastgdelstseen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usrinfo',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='chat.room'),
        ),
        migrations.AlterField(
            model_name='usrinfo',
            name='guide_lastgdelstseen',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 9, 30, 7, 512019, tzinfo=utc)),
        ),
    ]
