# Generated by Django 3.0.3 on 2020-06-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0066_auto_20200607_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='senderName',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='groupchat',
            name='senderPic',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
