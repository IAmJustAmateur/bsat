# Generated by Django 3.0.3 on 2020-05-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200513_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='steaming',
            field=models.DurationField(verbose_name='пропарка, ч'),
        ),
    ]