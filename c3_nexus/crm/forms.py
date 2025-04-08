from django import forms
from .models import Contact, CustomerHistory, Lead

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'contact_type', 'company', 'email', 'phone', 'last_interaction', 'next_action']
        widgets = {
            'last_interaction': forms.DateInput(attrs={'type': 'date'}),
        }
class CustomerHistoryForm(forms.ModelForm):
    class Meta:
        model = CustomerHistory
        fields = ['customer', 'date', 'product', 'warranty_status', 'last_interaction', 'notes']

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['client_name', 'current_stage', 'sales_rep', 'last_contact_date']  
