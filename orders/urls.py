from django.urls import path, include
from django.contrib.auth import views as auth_views
from orders.views import (CleaningCreateView, CleaningDeleteView, CleaningDetailView, CleaningListView, CleaningUpdateView)

app_name = 'orders'

urlpatterns = [
    path('', CleaningListView.as_view(), name = 'cleaning_list'),
    path('<int:pk>/',CleaningDetailView.as_view(), name='cleaning_detail'),
    path('create/', CleaningCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CleaningUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CleaningDeleteView.as_view(), name='delete')  
]