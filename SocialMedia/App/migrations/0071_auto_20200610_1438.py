# Generated by Django 3.0.3 on 2020-06-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0070_auto_20200610_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='dOB',
            field=models.DateField(blank=True),
        ),
    ]
