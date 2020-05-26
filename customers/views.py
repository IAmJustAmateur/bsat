from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from . models import Customer
from django.views.generic import (View, TemplateView, ListView,
                                    DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.
class CustomerListView(ListView):
    context_object_name='customer_list'
    model = Customer

class CustomerDetailView(DetailView):
    context_object_name='customer_detail'
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_update_form'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customers")


