# Generated by Django 3.0.3 on 2020-06-13 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0073_comments_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='userInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.userRegistration'),
        ),
    ]
