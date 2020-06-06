# Generated by Django 3.0.6 on 2020-06-06 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0030_auto_20200604_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(blank=True, default='', max_length=100)),
                ('commentId', models.CharField(blank=True, default='', max_length=100)),
                ('comment', models.CharField(blank=True, default='', max_length=500)),
                ('commentedBy', models.CharField(blank=True, default='', max_length=500)),
                ('commentedOf', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
