from django.urls import path, include
from . import views
app_name = 't_order_bot'

urlpatterns = [
    path('', views.index, name = 't_order_bot'),
]