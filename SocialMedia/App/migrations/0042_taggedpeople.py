# Generated by Django 3.0.6 on 2020-06-22 11:49

import datetime
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0041_auto_20200621_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taggedId', models.CharField(blank=True, default='', max_length=50)),
                ('taggedPersons', django_mysql.models.ListCharField(models.CharField(blank=True, default='', max_length=50), max_length=10000, size=None)),
                ('postId', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]