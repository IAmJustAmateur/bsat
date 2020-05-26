from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from customers.models import Customer

class Team(models.Model):
    name = models.CharField(max_length = 120)
    
    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length = 120)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 120)
    cleaning_technology = models.TextField(max_length = 255)

    def __str__(self):
        return self.name


class Add_work(models.Model):
    work = models.CharField(max_length = 120)

    def __str__(self):
        return self.work

class Car_Num(models.Model):
    num = models.CharField(max_length=10)

    def __str__(self):
        return self.num

class Car_Type(models.Model):
    car_type = models.CharField(max_length=30)

    def __str__(self):
        return self.car_type

class Tank_Num(models.Model):
    num = models.CharField(max_length=15)

    def __str__(self):
        return self.num


class Trail_Type(models.Model):
    trail_type = models.CharField(max_length=30)

    def __str__(self):
        return self.trail_type

# class Section_Field(models.FloatField):
    
#     blank=True
#     null = True
#     validators=[MaxValueValidator(40), MinValueValidator(0)]
#     help_text = "Объем секции, м3"
#     error_text = "Недопустимый объем секции"

    
class Order_registry(models.Model):
    month = models.CharField(max_length = 2)
    year = models.CharField(max_length = 4)

    def __str__(self):
        return self.month+"/"+self.year   
   


class Order(models.Model):
    registry = models.ForeignKey(Order_registry, on_delete = models.CASCADE, verbose_name = "Журнал моек", default = 1)

    customer_name = models.ForeignKey(Customer, on_delete = models.CASCADE, verbose_name = 'Заказчик')

    cleaning_date_start = models.DateField(verbose_name = 'Дата', auto_now=True)
    cleaning_date_end = models.DateField(verbose_name = 'Дата окончания', blank=True, null = True)
    cleaning_time_start = models.TimeField(verbose_name = 'Время начала', blank=True, null = True)
    cleaning_time_end = models.TimeField(verbose_name = 'Время окончания', blank=True, null = True)

    team = models.ForeignKey(Team, on_delete = models.CASCADE, verbose_name = 'Смена')

    driver_name = models.ForeignKey(Driver, on_delete = models.CASCADE, verbose_name = 'Водитель', blank=True)

    external_cleaning = models.BooleanField(verbose_name = 'Наружная мойка')

    car_type = models.ForeignKey(Car_Type, on_delete = models.CASCADE, null=True, blank = True)
    car_num = models.ForeignKey(Car_Num, on_delete=models.CASCADE, verbose_name = 'Номер машины', null=True, blank = True)
    car_cleaning_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    
    trail_type = models.ForeignKey(Trail_Type, on_delete = models.CASCADE, blank = True, null = True)
    tank_num = models.ForeignKey(Tank_Num, on_delete=models.CASCADE, verbose_name = 'Номер полуприцепа/контейнера',  blank = True, null = True)
    trail_cleaning_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

    internal_cleaning = models.BooleanField(verbose_name = 'Внутренняя мойка цистерны')

    steaming = models.TimeField(verbose_name='пропарка, ч')
    steaming_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

    add_work = models.ForeignKey(Add_work, on_delete = models.CASCADE, blank=True, null=True, verbose_name = 'Доп работы')
    add_work_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

    #sections
    sec1 = models.FloatField(blank = True, null = True, validators=[MaxValueValidator(40), MinValueValidator(0)])
    sec2 = models.FloatField(blank = True, null = True, validators=[MaxValueValidator(40), MinValueValidator(0)])
    sec3 = models.FloatField(blank = True, null = True, validators=[MaxValueValidator(40), MinValueValidator(0)])
    sec4 = models.FloatField(blank = True, null = True, validators=[MaxValueValidator(40), MinValueValidator(0)])
    sec5 = models.FloatField(blank = True, null = True, validators=[MaxValueValidator(40), MinValueValidator(0)])
    sec6 = models.FloatField(blank = True, null = True, validators=[MaxValueValidator(40), MinValueValidator(0)])

    internal_cleaning_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

    desinfection = models.BooleanField(verbose_name='Дезинфекция', default=False)
    desinfection_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

    total_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    
    paid = models.BooleanField(verbose_name='Оплачено', default=False)

    billed = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse("orders:order_list")

    def __str__(self):
        return "мойка: {0} {1} {2} {3}".format( self.customer_name, self.team, self.driver_name, self.car_num)
    