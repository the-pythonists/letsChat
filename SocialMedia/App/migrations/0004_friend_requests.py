# Generated by Django 3.0.3 on 2020-05-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200505_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend_Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderId', models.CharField(default='', max_length=50)),
                ('receiverId', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
