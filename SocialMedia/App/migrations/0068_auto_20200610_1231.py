# Generated by Django 3.0.3 on 2020-06-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0067_auto_20200608_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='userName',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]