from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from . import forms
from . models import (Order, Team, Driver, Add_work)
from django.views.generic import (View, TemplateView, ListView,
                                    DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.
class OrderListView(ListView):
    context_object_name='order_list'
    model = Order

class OrderDetailView(DetailView):
    context_object_name='order_detail'
    model = Order

class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'

class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("orders")
