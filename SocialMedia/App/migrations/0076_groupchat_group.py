# Generated by Django 3.0.3 on 2020-06-15 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0075_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='Group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.Groups'),
        ),
    ]
