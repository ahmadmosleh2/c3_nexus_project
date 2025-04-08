from django.urls import path
from .views import inventory_overview, export_inventory_csv

urlpatterns = [
    path('', inventory_overview, name='inventory'),
    path('inventory/export/', views.export_inventory_csv, name='export_inventory'),

]
