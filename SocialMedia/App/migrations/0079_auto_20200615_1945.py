# Generated by Django 3.0.3 on 2020-06-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0078_auto_20200615_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='Inbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Inbox'),
        ),
    ]
