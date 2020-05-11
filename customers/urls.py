from django.urls import path, include
from django.contrib.auth import views as auth_views
#from . import views
from customers.views import (CustomerListView, CustomerDetailView, CustomerCreateView,
                            CustomerUpdateView, CustomerDeleteView)

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name = 'customer_list'),
    path('<int:pk>/',CustomerDetailView.as_view(), name='customer_detail'),
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete')  
]