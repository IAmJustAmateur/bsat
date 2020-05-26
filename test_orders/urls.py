from django.urls import path
from django.contrib.auth import views as auth_views
from test_orders.views import (Test_OrderCreateView, Test_OrderUpdateView, Test_OrderDetailView, Test_OrderListView)

app_name = 'test_orders'

urlpatterns = [
    path('', Test_OrderListView.as_view(), name = 'test_order_list'),
    path('<int:pk>/',Test_OrderDetailView.as_view(), name='test_order_detail'),
    path('create/', Test_OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>', Test_OrderUpdateView.as_view(), name='update'),
]