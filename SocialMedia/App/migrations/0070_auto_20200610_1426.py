# Generated by Django 3.0.3 on 2020-06-10 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0069_auto_20200610_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='joinedDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
