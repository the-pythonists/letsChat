# Generated by Django 3.0.3 on 2020-06-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0085_userpost_posttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='AlbumID',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
