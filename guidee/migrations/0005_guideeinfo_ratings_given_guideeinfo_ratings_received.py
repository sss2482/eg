# Generated by Django 4.0.3 on 2022-04-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0005_rating_status'),
        ('guidee', '0004_rename_rvws_post_guideeinfo_rvws_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideeinfo',
            name='ratings_given',
            field=models.ManyToManyField(related_name='guidee_rated', to='entry.rating'),
        ),
        migrations.AddField(
            model_name='guideeinfo',
            name='ratings_received',
            field=models.ManyToManyField(related_name='guidee_received', to='entry.rating'),
        ),
    ]
