# Generated by Django 3.0.3 on 2020-05-17 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0038_auto_20200517_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(default='', max_length=50)),
                ('media', models.ImageField(blank=True, upload_to='profiles')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
