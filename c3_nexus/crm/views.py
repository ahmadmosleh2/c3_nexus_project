from django.shortcuts import render

# Create your views here.
def crm_overview(request):
    contacts = [
        {'id': 'C-101', 'name': 'John Smith', 'type': 'Customer', 'company': 'N/A', 'email': 'john@email.com',
         'phone': '(555) 123-4567', 'last_interaction': '2024-06-10', 'next_action': 'Follow-up Call'},
        {'id': 'D-202', 'name': 'XYZ Auto', 'type': 'Dealership', 'company': 'XYZ Auto Group', 'email': 'xyz@email.com',
         'phone': '(555) 987-6543', 'last_interaction': '2024-06-25', 'next_action': 'Schedule Inspection'},
        {'id': 'C-103', 'name': 'Emily Davis', 'type': 'Customer', 'company': 'N/A', 'email': 'emily@email.com',
         'phone': '(555) 555-5555', 'last_interaction': '2024-06-12', 'next_action': 'Warranty Activation'},
        {'id': 'D-204', 'name': 'LMN Cars', 'type': 'Dealership', 'company': 'LMN Motors', 'email': 'lmn@email.com',
         'phone': '(555) 222-3333', 'last_interaction': '2024-06-05', 'next_action': 'Inventory Review'},
        {'id': 'D-204', 'name': 'Alexa Amazon', 'type': 'Dealership', 'company': 'Lexa Lexus', 'email': 'legta@email.com',
         'phone': '(555) 295-2968', 'last_interaction': '2025-06-12', 'next_action': 'Follow-up Call'},
    ]
    
    return render(request, 'crm/crm_overview.html', {'contacts': contacts})


def customer_history(request):
    customer_history_data = [
        {'date': '2025-02-10', 'name': 'John Smith (Customer)', 'product': 'Paint Sealer',
         'dealership': 'ABC MOTORS', 'warranty_status': 'Active', 'last_interaction': '2025-02-12 - Email',
         'notes': 'Requested early check-up'},

        {'date': '2025-01-28', 'name': 'XYZ Auto (Dealership)', 'product': 'Rust Protection Package',
         'dealership': 'N/A', 'warranty_status': 'Expired', 'last_interaction': '2025-02-05 - Call',
         'notes': 'Needs renewal guidance'},

        {'date': '2024-12-20', 'name': 'Emily Davis (Customer)', 'product': 'VIN Etching Kit',
         'dealership': 'LMN Cars', 'warranty_status': 'Active', 'last_interaction': '2025-01-15 - Follow-up',
         'notes': 'Customer satisfied'},

        {'date': '2024-11-30', 'name': 'GHI Auto (Dealership)', 'product': 'Bulk Order - Fabric Guard',
         'dealership': 'N/A', 'warranty_status': 'Active', 'last_interaction': '2025-01-20 - Site Visit',
         'notes': 'Planning next bulk order'},

        {'date': '2024-10-15', 'name': 'Robert Chen (Customer)', 'product': 'Extended Warranty Plan',
         'dealership': 'DEF Dealership', 'warranty_status': 'Expired', 'last_interaction': '2025-02-01 - Email',
         'notes': 'Considering renewal'},
    ]

    return render(request, 'crm/customer_history.html', {'customer_history': customer_history_data})


def lead_tracking(request):
    leads = [
        {'name': 'Sarah Johnson', 'stage': 'Lead - Initial Contact', 'rep': 'Robert Chen', 'last_contact': '2025-02-10'},
        {'name': 'XYZ Auto', 'stage': 'Active Dealership', 'rep': 'Emily Davis', 'last_contact': '2025-01-25'},
        {'name': 'Michael Lee', 'stage': 'Converted - Purchased', 'rep': 'John Smith', 'last_contact': '2025-02-12'},
        {'name': 'LMN Cars', 'stage': 'Onboarding - In Process', 'rep': 'Jane Doe', 'last_contact': '2025-02-05'},
        {'name': 'Mark Anderson', 'stage': 'Negotiation - Proposal Sent', 'rep': 'Emily Davis', 'last_contact': '2025-02-08'},
        {'name': 'Mikey Boss', 'stage': 'Negotiation - Proposal Sent', 'rep': 'Amal Hope', 'last_contact': '2025-01-02'},
    ]
    return render(request, 'crm/lead_tracking.html', {'leads': leads})

def contacts(request):
    return render(request, 'crm.html', {'active_tab': 'contacts'})