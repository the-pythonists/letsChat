# Generated by Django 3.0.3 on 2020-05-12 11:44

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_auto_20200512_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allfriends',
            name='Friends',
            field=django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=10000, size=None),
        ),
    ]
