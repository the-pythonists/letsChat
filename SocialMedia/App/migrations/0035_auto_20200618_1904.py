# Generated by Django 3.0.6 on 2020-06-18 19:04

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_auto_20200618_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inboxId', models.CharField(blank=True, default='', max_length=50)),
                ('Users', django_mysql.models.ListCharField(models.CharField(blank=True, default='', max_length=50), max_length=10000, size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='messages',
            name='Users',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='inboxId',
        ),
        migrations.AddField(
            model_name='messages',
            name='Inbox',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.Inbox'),
            preserve_default=False,
        ),
    ]