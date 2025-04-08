from django.urls import path
from . import views

from .views import (
    crm_overview,
    customer_history,
    lead_tracking,
    contacts,
    add_contact,
    edit_contact,
    delete_contact,
    add_customer_history,
    add_lead
)

urlpatterns = [
    path('', crm_overview, name='crm'),  # This makes /crm/ work
    path('contacts/', contacts, name='contacts'),
    path('customer-history/', customer_history, name='customer_history'),
    path('lead-tracking/', lead_tracking, name='lead_tracking'),
    path('add-contact/', add_contact, name='add_contact'),
    path('edit-contact/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/', delete_contact, name='delete_contact'),
    path('add-customer-history/', add_customer_history, name='add_customer_history'),
    path('add-lead/', add_lead, name='add_lead'),
    path('export-contacts/', views.export_contacts_csv, name='export_contacts'),
    path('customer-history/', views.customer_history, name='customer_history'),
    path('export-history/', views.export_customer_history_csv, name='export_customer_history'),
    path('lead-tracking/', views.lead_tracking, name='lead_tracking'),
    path('export-leads/', views.export_leads_csv, name='export_leads_csv'),

]
