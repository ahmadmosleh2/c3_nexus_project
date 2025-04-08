from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from warranty.models import Claim
from .forms import ClaimForm
import csv
from django.http import HttpResponse
from django.db.models import Q



# Home page view
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect logged-in users
    return redirect('login')  # Redirect guests


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login

    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


@login_required
def claims_overview(request):
    search_query = request.GET.get("search", "")
    claims = Claim.objects.all()

    if search_query:
        claims = claims.filter(
            Q(dealership__icontains=search_query) |
            Q(product__icontains=search_query)
        )

    return render(request, 'claims.html', {
        'claims': claims,
        'search_query': search_query,
    })



def submit_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.user = request.user
            claim.save()
            return redirect('claims')  # Make sure this URL is correct
    else:
        form = ClaimForm()

    return render(request, 'claims.html', {'form': form})

# Sample Inventory Data (Replace this with real database query)
inventory_data = [
    {'id': 'INV-101', 'name': 'Anti-Theft', 'stock_level': 12, 'alert': 'LOW', 'dealership': 'Ontario Toyota', 'restock_date': '2024-05-17', 'restock_recommendation': 'Reorder: 20 units'},
    {'id': 'INV-102', 'name': 'Body', 'stock_level': 40, 'alert': 'IN STOCK', 'dealership': 'Quebec Dodge', 'restock_date': '2024-05-16', 'restock_recommendation': 'No Immediate Need'},
    {'id': 'INV-103', 'name': 'Chemical', 'stock_level': 34, 'alert': 'IN STOCK', 'dealership': 'GTA Lexus', 'restock_date': '2024-05-15', 'restock_recommendation': 'No Immediate Need'},
    {'id': 'INV-104', 'name': 'Drip', 'stock_level': 19, 'alert': 'LOW', 'dealership': 'Montreal Audi', 'restock_date': '2024-05-15', 'restock_recommendation': 'Reorder: 20 units'},
    {'id': 'INV-105', 'name': 'Extra Care', 'stock_level': 'N/A', 'alert': 'N/A', 'dealership': 'GTA Auto', 'restock_date': 'N/A', 'restock_recommendation': 'No Immediate Need'},
]

def inventory_overview(request):
    query = request.GET.get('q')

    inventory_data = [
        {'id': 'INV-101', 'name': 'Anti-Theft', 'stock_level': 12, 'alert': 'LOW', 'dealership': 'Ontario Toyota', 'restock_date': '2024-05-17', 'restock_recommendation': 'Reorder: 20 units'},
        {'id': 'INV-102', 'name': 'Body', 'stock_level': 40, 'alert': 'IN STOCK', 'dealership': 'Quebec Dodge', 'restock_date': '2024-05-16', 'restock_recommendation': 'No Immediate Need'},
        {'id': 'INV-103', 'name': 'Chemical', 'stock_level': 34, 'alert': 'IN STOCK', 'dealership': 'GTA Lexus', 'restock_date': '2024-05-15', 'restock_recommendation': 'No Immediate Need'},
        {'id': 'INV-104', 'name': 'Drip', 'stock_level': 19, 'alert': 'LOW', 'dealership': 'Montreal Audi', 'restock_date': '2024-05-15', 'restock_recommendation': 'Reorder: 20 units'},
        {'id': 'INV-105', 'name': 'Extra Care', 'stock_level': 'N/A', 'alert': 'N/A', 'dealership': 'GTA Auto', 'restock_date': 'N/A', 'restock_recommendation': 'No Immediate Need'},
    ]

    # Filter by search query
    if query:
        query = query.lower()
        inventory_data = [
            item for item in inventory_data
            if query in item['name'].lower() or query in item['dealership'].lower()
        ]

    return render(request, 'users/inventory.html', {'inventory': inventory_data})
def export_inventory_csv(request):
    query = request.GET.get('q')
    filter_option = request.GET.get('filter')

    # Build the same inventory list as inventory_overview does
    inventory_data = [
        {'id': 'INV-101', 'name': 'Anti-Theft', 'stock_level': 12, 'alert': 'LOW', 'dealership': 'Ontario Toyota', 'restock_date': '2024-05-17', 'restock_recommendation': 'Reorder: 20 units'},
        {'id': 'INV-102', 'name': 'Body', 'stock_level': 40, 'alert': 'IN STOCK', 'dealership': 'Quebec Dodge', 'restock_date': '2024-05-16', 'restock_recommendation': 'No Immediate Need'},
        {'id': 'INV-103', 'name': 'Chemical', 'stock_level': 34, 'alert': 'IN STOCK', 'dealership': 'GTA Lexus', 'restock_date': '2024-05-15', 'restock_recommendation': 'No Immediate Need'},
        {'id': 'INV-104', 'name': 'Drip', 'stock_level': 19, 'alert': 'LOW', 'dealership': 'Montreal Audi', 'restock_date': '2024-05-15', 'restock_recommendation': 'Reorder: 20 units'},
        {'id': 'INV-105', 'name': 'Extra Care', 'stock_level': 'N/A', 'alert': 'N/A', 'dealership': 'GTA Auto', 'restock_date': 'N/A', 'restock_recommendation': 'No Immediate Need'},
    ]

    # Optional filtering if desired
    if query:
        inventory_data = [
            item for item in inventory_data
            if query.lower() in item['name'].lower() or query.lower() in item['dealership'].lower()
        ]
    if filter_option == 'low':
        inventory_data = [item for item in inventory_data if item['alert'] == 'LOW']
    elif filter_option == 'recent':
        inventory_data = [item for item in inventory_data if item['restock_date'] and str(item['restock_date']).startswith("2024")]

    # Export
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Product ID', 'Product Name', 'Stock Level', 'Low Stock Alert', 'Assigned Dealership', 'Last Restocked Date', 'Restock Recommendation'])

    for item in inventory_data:
        writer.writerow([
            item['id'],
            item['name'],
            item['stock_level'],
            item['alert'],
            item['dealership'],
            item['restock_date'],
            item['restock_recommendation'],
        ])

    return response


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
    return render(request, 'crm/crm.html', {'contacts': contacts})


@login_required
def export_sales_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dashboard_export.csv"'

    writer = csv.writer(response)
    
    # First section: Sales by Month
    writer.writerow(['Monthly Sales Overview'])
    writer.writerow(['Month', 'Sales', 'Revenue', 'Finance Balance'])

    sales_data = [
        ['January', 100, 4000, 12243],
        ['February', 120, 4500, ''],
        ['March', 150, 5000, ''],
        ['April', 170, 5200, ''],
        ['May', 200, 5313, ''],
        ['June', 220, 5000, ''],
    ]

    for row in sales_data:
        writer.writerow(row)

    # Spacer row
    writer.writerow([])

    # Second section: Top 3 Selling Items
    writer.writerow(['Top 3 Selling Items'])
    writer.writerow(['Item', 'Revenue'])

    top_items = [
        ['Item 1', 50],
        ['Item 2', 75],
        ['Item 3', 100],
    ]

    for item in top_items:
        writer.writerow(item)

    return response

@login_required
def export_claims_csv(request):
    # Create HTTP response with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="claims.csv"'

    # Create CSV writer
    writer = csv.writer(response)
    writer.writerow(['Claim ID', 'Date Submitted', 'Customer', 'Dealership', 'Product', 'Status', 'Amount', 'Last Updated'])

    # Query all claims
    claims = Claim.objects.all()

    for claim in claims:
        writer.writerow([
            claim.id,
            claim.claim_date.strftime('%Y-%m-%d'),
            claim.user.username,
            claim.dealership,
            claim.product,
            claim.get_status_display(),
            f"${claim.amount}",
            claim.last_updated.strftime('%Y-%m-%d %H:%M')
        ])

    return response
    