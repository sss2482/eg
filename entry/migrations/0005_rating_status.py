# Generated by Django 4.0.3 on 2022-04-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0004_alter_review_status_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='status',
            field=models.CharField(default='gde_gd', max_length=15),
        ),
    ]