from django.urls import path
from .views import inventory_list, add_medicine, edit_medicine, delete_medicine, dashboard, requisition, forecasting, user_management

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('add/', add_medicine, name='add_medicine'),
    path('edit/<int:pk>/', edit_medicine, name='edit_medicine'),
    path('delete/<int:pk>/', delete_medicine, name='delete_medicine'),
    path('dashboard/', dashboard, name='dashboard'),
    path('requisition/', requisition, name='requisition'),
    path('forecasting/', forecasting, name='forecasting'),
    path('user_management/', user_management, name='user_management'),
]
