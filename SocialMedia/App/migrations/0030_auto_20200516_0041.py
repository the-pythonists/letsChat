# Generated by Django 3.0.3 on 2020-05-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_userpost_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='userPic',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
