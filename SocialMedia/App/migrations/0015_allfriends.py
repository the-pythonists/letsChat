# Generated by Django 3.0.3 on 2020-05-12 06:12

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_auto_20200512_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('Friends', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=1000, size=None)),
            ],
        ),
    ]
