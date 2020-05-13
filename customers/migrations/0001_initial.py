# Generated by Django 3.0.3 on 2020-05-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, unique=True, verbose_name='Наименование')),
                ('short_name', models.CharField(max_length=120, unique=True, verbose_name='Наименование Краткое')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Наименование Полное')),
                ('legal_address', models.CharField(blank=True, max_length=255, verbose_name='Адрес Юридический')),
                ('post_address', models.CharField(blank=True, max_length=255, verbose_name='Адрес Почтовый')),
                ('tax_id', models.CharField(blank=True, max_length=30, unique=True, verbose_name='УНП')),
                ('bank', models.CharField(blank=True, max_length=100)),
                ('bank_acc', models.CharField(blank=True, max_length=100)),
                ('BIC', models.CharField(blank=True, max_length=100)),
                ('bank_addr', models.CharField(blank=True, max_length=100)),
                ('contract_num', models.CharField(blank=True, max_length=10)),
                ('contract_date', models.DateField(blank=True, null=True)),
                ('director_name', models.CharField(blank=True, max_length=120)),
                ('contact_name', models.CharField(blank=True, max_length=120)),
                ('contact_position', models.CharField(blank=True, max_length=120)),
                ('phone', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('other_info', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
