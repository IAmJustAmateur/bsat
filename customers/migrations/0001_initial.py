# Generated by Django 3.0.3 on 2020-05-07 05:04

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
                ('name', models.CharField(blank=True, max_length=120)),
                ('short_name', models.CharField(max_length=120)),
                ('full_name', models.CharField(blank=True, max_length=120)),
                ('legal_address', models.CharField(blank=True, max_length=255)),
                ('post_address', models.CharField(blank=True, max_length=255)),
                ('tax_id', models.CharField(blank=True, max_length=30)),
                ('bank', models.CharField(blank=True, max_length=100)),
                ('bank_acc', models.CharField(blank=True, max_length=100)),
                ('BIC', models.CharField(blank=True, max_length=100)),
                ('bank_addr', models.CharField(blank=True, max_length=100)),
                ('contract_num', models.CharField(blank=True, max_length=10)),
                ('contract_date', models.DateField(blank=True)),
                ('director_name', models.CharField(blank=True, max_length=120)),
                ('contact_name', models.CharField(blank=True, max_length=120)),
                ('contact_position', models.CharField(blank=True, max_length=120)),
                ('phone', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('other_info', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
