# Generated by Django 3.0.3 on 2020-05-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currensy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, unique=True, verbose_name='Валюта')),
                ('symbol', models.CharField(max_length=5, unique=True, verbose_name='Обозначение')),
            ],
        ),
    ]
