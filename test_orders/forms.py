from . models import Test_Order
from django import forms
from customers.models import Customer
import datetime

# def my_date():
#     return datetime.date()

class Test_OrderForm(forms.Form):
    number = forms.IntegerField(label='Номер:')
    cleaning_date_start = forms.DateField(label = 'Дата:', initial = datetime.date.today())
    customer_name = forms.ModelChoiceField(label='Заказчик', queryset=Customer.objects.all())
    volume = forms.FloatField(label='Объем')

