# Generated by Django 3.0.6 on 2020-06-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0036_auto_20200620_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='PhotoType',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
