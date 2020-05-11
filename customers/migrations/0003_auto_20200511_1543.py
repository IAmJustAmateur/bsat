# Generated by Django 3.0.3 on 2020-05-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200508_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Наименование Полное'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='legal_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес Юридический'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='post_address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес Почтовый'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='short_name',
            field=models.CharField(max_length=120, verbose_name='Наименование Краткое'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tax_id',
            field=models.CharField(blank=True, max_length=30, verbose_name='УНП'),
        ),
    ]
