# Generated by Django 3.0.3 on 2020-05-30 10:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_auto_20200519_0728'),
        ('test_orders', '0002_auto_20200524_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_order',
            name='cleaning_date_start',
            field=models.DateField(default=datetime.datetime(2020, 5, 30, 13, 52, 53, 713750), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='test_order',
            name='customer_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer', verbose_name='Заказчик'),
        ),
    ]