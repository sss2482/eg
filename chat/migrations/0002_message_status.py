# Generated by Django 4.0.3 on 2022-04-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
