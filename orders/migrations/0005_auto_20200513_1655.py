# Generated by Django 3.0.3 on 2020-05-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('orders', '0004_auto_20200513_1629'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cleaning',
            new_name='Order',
        ),
    ]
