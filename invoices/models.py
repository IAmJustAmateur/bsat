from django.db import models
from customers.models import Customer
from orders.models import Order

# Create your models here.
class Document(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    document_date = models.DateField()
    document_number = models.CharField(max_length=10)

    amount = models.DecimalField(max_digits = 6, decimal_places=2)
    works = []
