from django.urls import path
from .views import home, user_login, user_logout, dashboard
from django.urls import path
from .views import user_login, register
from .views import user_logout, user_login, dashboard, claims_overview 
from .views import claims_overview, submit_claim
from .views import inventory_overview
from .views import crm_overview
from .views import export_sales_data
from .views import export_claims_csv
from . import views



urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),  
    path('claims/', claims_overview, name='claims'),
path('claims/submit/', submit_claim, name='submit_claim'),
    path('inventory/', inventory_overview, name='inventory'),
    path('', crm_overview, name='crm'),
    path('export-sales-data/', export_sales_data, name='export_sales'),
    path('claims/export/', export_claims_csv, name='export_claims'),
    path('inventory/export/', views.export_inventory_csv, name='export_inventory'),
    
    
    
]



