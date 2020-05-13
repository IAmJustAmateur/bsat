# Generated by Django 3.0.3 on 2020-05-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='cleaning_date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='cleaning_time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Время окончания'),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='cleaning_time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Время начала'),
        ),
    ]