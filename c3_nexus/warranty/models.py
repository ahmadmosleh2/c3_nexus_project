from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from users.models import CustomUser
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Claim(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    claim_date = models.DateTimeField(default=now)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Claim {self.id} - {self.status}"


class Claim(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="warranty_claims"  
    )
    dealership = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    claim_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Warranty Claim {self.id} - {self.status}"
