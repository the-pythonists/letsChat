# Generated by Django 3.0.3 on 2020-05-18 11:42

import datetime
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_auto_20200515_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=55)),
                ('sender', models.CharField(blank=True, max_length=55)),
                ('receiver', models.CharField(blank=True, max_length=55)),
                ('notification', models.CharField(blank=True, max_length=100)),
                ('viewed', models.BooleanField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(default='', max_length=50)),
                ('media', models.ImageField(blank=True, upload_to='profiles')),
                ('uploadTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.RenameField(
            model_name='friend_requests',
            old_name='receiverId',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='friend_requests',
            old_name='senderId',
            new_name='sender',
        ),
        migrations.AddField(
            model_name='friend_requests',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='allfriends',
            name='Friends',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=50), max_length=10000, size=None),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='userPic',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
