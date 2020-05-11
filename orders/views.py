from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from . import forms
from . models import (Cleaning, Team, Driver, Add_work)
from django.views.generic import (View, TemplateView, ListView,
                                    DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.
class CleaningListView(ListView):
    context_object_name='cleaning_list'
    model = Cleaning

class CleaningDetailView(DetailView):
    context_object_name='cleaning_detail'
    model = Cleaning

class CleaningCreateView(CreateView):
    model = Cleaning
    fields = '__all__'

class CleaningUpdateView(UpdateView):
    model = Cleaning
    fields = '__all__'

class CleaningDeleteView(DeleteView):
    model = Cleaning
    success_url = reverse_lazy("cleanings")