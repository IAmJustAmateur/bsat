from django import forms
from . models import (Cleaning, Add_work, Team, Driver)

class CleaningForm(forms.ModelForm):
    class Meta:
        fields ='__all__'
        model = Cleaning

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

