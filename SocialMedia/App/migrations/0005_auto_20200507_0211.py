# Generated by Django 3.0.3 on 2020-05-06 20:41

import App.views
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_friend_requests'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(default='194734ef5ff54dbaa258cb0168331ec0', max_length=100)),
                ('userId', models.CharField(default='', max_length=50)),
                ('post', models.ImageField(upload_to='profiles')),
                ('Message', models.CharField(default='', max_length=5000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='friend_requests',
            name='senderName',
            field=models.CharField(default='', max_length=75),
        ),
    ]
