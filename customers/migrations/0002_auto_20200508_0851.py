# Generated by Django 3.0.3 on 2020-05-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contract_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
