from django.db import models
from django.urls import reverse, resolve

from customers.models import Customer

class Team(models.Model):
    name = models.TextField(max_length = 120)

class Driver(models.Model):
    name = models.TextField(max_length = 120)

class Add_work(models.Model):
    work = models.TextField(max_length = 120)

class Cleaning(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete = models.CASCADE, verbose_name = 'Заказчик')
    cleaning_date_start = models.DateField(verbose_name = 'Дата')
    cleaning_date_end = models.DateField(verbose_name = 'Дата окончания')
    cleaning_time_start = models.TimeField(verbose_name = 'Время начала')
    cleaning_time_end = models.TimeField(verbose_name = 'Время окончания')

    team = models.ForeignKey(Team, on_delete = models.CASCADE, verbose_name = 'Смена')

    driver_name = models.ForeignKey(Driver, on_delete = models.CASCADE, verbose_name = 'Водитель', blank=True)
    
    external_cleaning = models.BooleanField(verbose_name = 'Наружная мойка')

    internal_cleaning = models.BooleanField(verbose_name = 'Внутренняя мойка цистерны')

    steaming = models.TimeField(verbose_name='пропарка, ч')

    add_work = models.ForeignKey(Add_work, on_delete = models.CASCADE, blank=True, null=True)


    


# Create your models here.
