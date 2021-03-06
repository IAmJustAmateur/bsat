# Generated by Django 3.0.3 on 2020-05-19 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0010_auto_20200519_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_date', models.DateField()),
                ('document_number', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
    ]
