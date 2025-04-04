from django.urls import path
from .views import crm_overview, customer_history, lead_tracking, contacts

urlpatterns = [
    path('', crm_overview, name='crm'),
    path('', contacts, name='contacts'),
    path('customer-history/', customer_history, name='customer_history'),
    path('lead-tracking/', lead_tracking, name='lead_tracking'),
]
