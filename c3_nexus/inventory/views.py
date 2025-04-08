from django.shortcuts import render

# Create your views here.
from .models import InventoryItem
import csv
from django.http import HttpResponse
from inventory.models import InventoryItem

@login_required
def inventory_overview(request):
    query = request.GET.get('q')
    filtered_data = INVENTORY_DATA

    if query:
        filtered_data = [
            item for item in INVENTORY_DATA
            if query.lower() in item['name'].lower() or query.lower() in item['dealership'].lower()
        ]

    return render(request, 'inventory.html', {'inventory': filtered_data})

@login_required
def export_inventory_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Product ID', 'Product Name', 'Stock Level', 'Low Stock Alert', 'Assigned Dealership', 'Last Restocked Date', 'Restock Recommendation'])

    for item in INVENTORY_DATA:  # Use your list of dicts
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

