# Generated by Django 3.0.3 on 2020-06-07 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0065_auto_20200607_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupchat',
            old_name='message',
            new_name='Message',
        ),
    ]