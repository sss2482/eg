# Generated by Django 4.0.3 on 2022-06-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_rename_nid_fields_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ans',
            field=models.TextField(blank=True, null=True),
        ),
    ]
