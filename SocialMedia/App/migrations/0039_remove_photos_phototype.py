# Generated by Django 3.0.6 on 2020-06-21 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0038_auto_20200621_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='PhotoType',
        ),
    ]