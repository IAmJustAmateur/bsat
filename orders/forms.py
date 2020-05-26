from django import forms
from . models import (Order, Add_work, Team, Driver)
from customers.models import Customer

# class OrderForm(forms.ModelForm):
#     class Meta:
#         fields ='__all__'
#         model = Order

class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())

class Add_work_Form(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Add_work

class DriverForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Driver

class TeamForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Team

# class OrderForm(forms.Form):
#     product = forms.ModelChoiceField(queryset=Product.objects.all()) # with queryset you can show a checkbox with the query
#     quantify = forms.IntegerField()