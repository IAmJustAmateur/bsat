from django.db import models
from django.urls import reverse, resolve

# Create your models here.

class Customer(models.Model):
    # name
    name = models.CharField(max_length = 120, blank=True, verbose_name='Наименование', unique=True)
    short_name = models.CharField(max_length = 120, verbose_name='Наименование Краткое', unique=True)
    full_name = models.CharField(max_length = 120, blank=True, verbose_name='Наименование Полное', unique=True)

    # address
    legal_address = models.CharField(max_length=255, blank=True, verbose_name='Адрес Юридический')
    post_address = models.CharField(max_length=255, blank=True, verbose_name='Адрес Почтовый')

    # tax id
    tax_id = models.CharField(max_length=30, blank=True, verbose_name='УНП', unique=True)

    # bank details
    bank  = models.CharField(max_length=100, blank=True)
    bank_acc =  models.CharField(max_length=100, blank=True)
    BIC = models.CharField(max_length=100, blank=True)
    bank_addr = models.CharField(max_length=100, blank=True)

    # contract
    contract_num = models.CharField(max_length=10, blank=True)
    contract_date = models.DateField(blank=True, null=True)

    # director
    director_name = models.CharField(max_length=120, blank=True)

    # contacts
    contact_name = models.CharField(max_length=120, blank=True)
    contact_position = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=120, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    # currency

    # payment type

    # other info
    other_info = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse("customers:customer_list")

    def __str__(self):
        return self.name






