# Generated by Django 3.0.3 on 2020-05-19 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20200519_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pmt_type',
            field=models.ForeignKey(default='other', on_delete=django.db.models.deletion.CASCADE, to='customers.Payment_Types'),
        ),
    ]
