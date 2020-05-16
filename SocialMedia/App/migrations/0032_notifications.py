# Generated by Django 3.0.3 on 2020-05-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0031_auto_20200517_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=55)),
                ('fullName', models.CharField(max_length=55)),
                ('sender', models.CharField(max_length=55)),
                ('receiver', models.CharField(max_length=55)),
                ('notification', models.CharField(max_length=55)),
                ('viewed', models.BooleanField()),
                ('userId', models.CharField(max_length=55)),
            ],
        ),
    ]
