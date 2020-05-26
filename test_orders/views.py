from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from . import forms
from . models import Test_Order
from django.views.generic import (View, TemplateView, ListView,
                                    DetailView, CreateView, UpdateView, DeleteView)

class Test_OrderCreateView(CreateView):
    model = Test_Order
    fields = '__all__'

class Test_OrderUpdateView(UpdateView):
    model = Test_Order
    # success_url='test_order_list'
    fields = '__all__'
    template_name_suffix = '_update_form'

class Test_OrderListView(ListView):
    context_object_name = 'test_order_list'
    model = Test_Order

class Test_OrderDetailView(DetailView):
    model = Test_Order
    context_object_name='test_order_detail'