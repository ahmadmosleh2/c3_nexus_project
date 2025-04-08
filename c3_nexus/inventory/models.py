from django.db import models

# Create your models here.

class InventoryItem(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    stock_level = models.CharField(max_length=20, null=True, blank=True)
    dealership = models.CharField(max_length=100)
    last_restocked = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"

    def low_stock_status(self):
        try:
            stock_num = int(self.stock_level.split()[0])
            return "LOW" if stock_num < 20 else "IN STOCK"
        except:
            return "N/A"

    def restock_recommendation(self):
        return "Reorder: 20 units" if self.low_stock_status() == "LOW" else "No Immediate Need"
