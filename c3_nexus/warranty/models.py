from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Claim(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='warranty_claims'
    )
    dealership = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    claim_date = models.DateTimeField(default=now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Warranty Claim {self.id} - {self.status}"
