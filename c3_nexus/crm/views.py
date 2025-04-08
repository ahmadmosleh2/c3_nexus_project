from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, CustomerHistory, Lead
from .forms import ContactForm, CustomerHistoryForm, LeadForm
from .models import Contact, Lead, CustomerHistory
import csv
from django.http import HttpResponse
from .models import Contact
from django.db.models import Q


# Create Contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new contact to the database
            return redirect('crm')   # Redirect to a page where all contacts are listed
    else:
        form = ContactForm()

    return render(request, 'crm/add_contact.html', {'form': form})

# Edit Contact
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('crm')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'crm/edit_contact.html', {'form': form})

# Delete Contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('crm')

# Add Customer History
def add_customer_history(request):
    if request.method == 'POST':
        form = CustomerHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_history')
    else:
        form = CustomerHistoryForm()
    return render(request, 'crm/add_customer_history.html', {'form': form})

# Add Lead
def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_tracking')
    else:
        form = LeadForm()
    return render(request, 'crm/add_lead.html', {'form': form})

# crm/views.py
from django.shortcuts import render

def customer_history(request):
    history = CustomerHistory.objects.all()


    query = request.GET.get('search')
    if query:
        history = history.filter(
            Q(customer__name__icontains=query) |
            Q(customer__company__icontains=query) |
            Q(product__icontains=query) |
            Q(notes__icontains=query)
        )

    
    year_filter = request.GET.get('year')
    if year_filter:
        history = history.filter(date__year=year_filter)

    return render(request, 'crm/customer_history.html', {'history': history})


def lead_tracking(request):
    leads = Lead.objects.all()  # Retrieve all Lead records
    return render(request, 'crm/lead_tracking.html', {'leads': leads})

def contacts(request):
    # Your logic for contacts page
    return render(request, 'crm/contacts.html')

def crm_dashboard(request):
    contacts = Contact.objects.all()
    leads = Lead.objects.all()
    customer_history = CustomerHistory.objects.all()

    return render(request, 'crm/crm_dashboard.html', {
        'contacts': contacts,
        'leads': leads,
        'history': customer_history,
    })
def crm_overview(request):
    contacts = Contact.objects.all()

    # Optional: Filter by year and search
    query = request.GET.get('search')
    year_filter = request.GET.get('year')

    if query:
        contacts = contacts.filter(
            Q(name__icontains=query) |
            Q(company__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        )
    if year_filter:
        contacts = contacts.filter(last_interaction__year=year_filter)

    return render(request, 'crm/crm_overview.html', {'contacts': contacts})

def export_contacts_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Type', 'Company', 'Email', 'Phone', 'Last Interaction', 'Next Action'])

    for contact in Contact.objects.all():
        writer.writerow([
            contact.id,
            contact.name,
            contact.contact_type,
            contact.company,
            contact.email,
            contact.phone,
            contact.last_interaction,
            contact.next_action
        ])

    return response



def export_customer_history_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer_history.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Customer Name', 'Customer Type', 'Company', 'Product', 'Warranty Status', 'Last Interaction', 'Notes'])

    history = CustomerHistory.objects.all()
    for entry in history:
        writer.writerow([
            entry.date,
            entry.customer.name,
            entry.customer.type,
            entry.customer.company,
            entry.product,
            entry.warranty_status,
            entry.last_interaction,
            entry.notes
        ])

    return response


def lead_tracking(request):
    # Retrieve all Lead records
    leads = Lead.objects.all()

    # Handle search query
    query = request.GET.get('search')
    if query:
        leads = leads.filter(
            Q(client_name__icontains=query) |
            Q(current_stage__icontains=query) |
            Q(sales_rep__icontains=query)
        )

    # Handle year filter
    year_filter = request.GET.get('year')
    if year_filter:
        try:
            year = int(year_filter)
            leads = leads.filter(last_contact_date__year=year)
        except ValueError:
            pass  # If the year is invalid, do nothing
    
    return render(request, 'crm/lead_tracking.html', {'leads': leads})


def export_leads_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'

    writer = csv.writer(response)
    writer.writerow(['Client Name', 'Current Stage', 'Assigned Sales Rep', 'Last Contact Date'])

    # Export all leads
    leads = Lead.objects.all()
    for lead in leads:
        writer.writerow([lead.client_name, lead.current_stage, lead.sales_rep, lead.last_contact_date])

    return response