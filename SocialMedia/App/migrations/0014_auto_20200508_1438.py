# Generated by Django 3.0.3 on 2020-05-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_test_test1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test1',
            old_name='testField',
            new_name='testField1',
        ),
    ]
