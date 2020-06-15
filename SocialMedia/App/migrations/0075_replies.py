# Generated by Django 3.0.3 on 2020-06-14 06:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0074_auto_20200613_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(blank=True, default='', max_length=50)),
                ('commentId', models.CharField(blank=True, default='', max_length=50)),
                ('replyId', models.CharField(blank=True, default='', max_length=50)),
                ('repliedBy', models.CharField(blank=True, default='', max_length=50)),
                ('repliedOn', models.CharField(blank=True, default='', max_length=50)),
                ('reply', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('userInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.userRegistration')),
            ],
        ),
    ]
