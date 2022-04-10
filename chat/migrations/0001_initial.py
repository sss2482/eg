# Generated by Django 4.0.3 on 2022-04-10 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mssg', models.CharField(max_length=5000)),
                ('time_send', models.DateTimeField(auto_now_add=True)),
                ('time_received', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=500)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr1', to=settings.AUTH_USER_MODEL)),
                ('guidee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr2', to=settings.AUTH_USER_MODEL)),
                ('messages', models.ManyToManyField(to='chat.message')),
            ],
        ),
        migrations.CreateModel(
            name='grp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]