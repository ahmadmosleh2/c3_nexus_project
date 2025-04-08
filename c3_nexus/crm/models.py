from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    last_interaction = models.DateTimeField()
    next_action = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    company = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    last_interaction = models.DateField()
    next_action = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    product = models.CharField(max_length=100)
    warranty_status = models.CharField(max_length=50)
    last_interaction = models.CharField(max_length=100)
    notes = models.TextField()

class Lead(models.Model):
    client_name = models.CharField(max_length=100)
    current_stage = models.CharField(max_length=100)
    sales_rep = models.CharField(max_length=100)
    last_contact_date = models.DateField()

    def __str__(self):
        return self.client_name
