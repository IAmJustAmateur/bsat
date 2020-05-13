from django.db import models
from django.urls import reverse, resolve
from django.core.validators import MaxValueValidator

from customers.models import Customer

class Team(models.Model):
    name = models.TextField(max_length = 120)

class Driver(models.Model):
    name = models.TextField(max_length = 120)

class Add_work(models.Model):
    work = models.TextField(max_length = 120)

class Car_Num(models.Model):
    num = models.TextField(max_length=10)

class Car_Type(models.Model):
    car_type = models.TextField(max_length=30)

class Tank_Num(models.Model):
    num = models.TextField(max_length=15)

class Trail_Type(models.Model):
    trail_type = models.TextField(max_length=30)

class Cleaning(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete = models.CASCADE, verbose_name = 'Заказчик')
    cleaning_date_start = models.DateField(verbose_name = 'Дата',auto_now=True)
    cleaning_date_end = models.DateField(verbose_name = 'Дата окончания')
    cleaning_time_start = models.TimeField(verbose_name = 'Время начала')
    cleaning_time_end = models.TimeField(verbose_name = 'Время окончания')

    team = models.ForeignKey(Team, on_delete = models.CASCADE, verbose_name = 'Смена')

    driver_name = models.ForeignKey(Driver, on_delete = models.CASCADE, verbose_name = 'Водитель', blank=True)
    
    external_cleaning = models.BooleanField(verbose_name = 'Наружная мойка')

    car_type = models.ForeignKey(Car_Type, on_delete = models.CASCADE, null=True, blank = True)
    car_num = models.ForeignKey(Car_Num, on_delete=models.CASCADE, verbose_name = 'Номер машины', null=True, blank = True)
    
    trail_type = models.ForeignKey(Trail_Type, on_delete = models.CASCADE, blank = True, null = True)
    tank_num = models.ForeignKey(Tank_Num, on_delete=models.CASCADE, verbose_name = 'Номер полуприцепа/контейнера',  blank = True, null = True)


    internal_cleaning = models.BooleanField(verbose_name = 'Внутренняя мойка цистерны')

    steaming = models.TimeField(verbose_name='пропарка, ч')

    add_work = models.ForeignKey(Add_work, on_delete = models.CASCADE, blank=True, null=True, verbose_name = 'Доп работы')

    #sections
    sec1 = models.FloatField(default=0, validators=[MaxValueValidator(40)], max_length=5)
    sec2 = models.FloatField(default=0, validators=[MaxValueValidator(40)], max_length=5)
    sec3 = models.FloatField(default=0, validators=[MaxValueValidator(40)], max_length=5)
    sec4 = models.FloatField(default=0, validators=[MaxValueValidator(40)], max_length=5)
    sec5 = models.FloatField(default=0, validators=[MaxValueValidator(40)], max_length=5)
    sec6 = models.FloatField(default=0, validators=[MaxValueValidator(40)], max_length=5)


    


# Create your models here.
