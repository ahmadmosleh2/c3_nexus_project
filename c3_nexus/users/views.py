from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from .models import Claim
from .forms import ClaimForm


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


def claims_overview(request):
    claims = Claim.objects.all()  #Fetch all claims
    return render(request, 'users/claims.html', {'claims': claims})




def claims_overview(request):
    claims = Claim.objects.all()  # Fetch all claims from the database
    return render(request, 'claims.html', {'claims': claims})

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
    return render(request, 'users/inventory.html', {'inventory': inventory_data})


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
