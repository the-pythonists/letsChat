# Generated by Django 3.0.3 on 2020-05-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20200507_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='postId',
            field=models.CharField(default='8d898df617734915b9c633708c08972b', max_length=100),
        ),
    ]
