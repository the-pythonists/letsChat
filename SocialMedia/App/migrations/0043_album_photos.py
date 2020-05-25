# Generated by Django 3.0.3 on 2020-05-18 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0042_auto_20200518_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]
