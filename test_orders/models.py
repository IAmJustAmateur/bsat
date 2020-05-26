from django.db import models

from customers.models import Customer
from django.urls import reverse, resolve
import datetime

# Create your models here.
class Test_Order(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete = models.CASCADE, verbose_name = 'Заказчик', default=1)
    cleaning_date_start = models.DateField(verbose_name = 'Дата', default = datetime.datetime.today())
    volume = models.FloatField(verbose_name = 'Объем')

    def get_absolute_url(self):
        return reverse("test_orders:test_order_list")

    def __str__(self):
        return "order: {0}, customer: {1}, date: {2}, volume: {3}".format (self.pk, self.customer_name, self.cleaning_date_start, self.volume)