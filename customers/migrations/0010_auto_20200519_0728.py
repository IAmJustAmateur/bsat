# Generated by Django 3.0.3 on 2020-05-19 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20200519_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='currency',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='customers.Currensy', verbose_name='валюта'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pmt_type',
            field=models.CharField(choices=[('every_time', 'Каждый раз по безналу'), ('once_a_month', 'Раз в месяц'), ('cash', 'черех кассу'), ('other', 'другое')], default='other', max_length=30, verbose_name='тип оплаты'),
        ),
        migrations.DeleteModel(
            name='Payment_Types',
        ),
    ]
