# Generated by Django 4.0.3 on 2022-04-21 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0012_alter_guideinfo_lastgdelstseen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guideinfo',
            old_name='rvws_post',
            new_name='rvws_posted',
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='lastgdelstseen',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 19, 54, 12, 852141, tzinfo=utc)),
        ),
    ]