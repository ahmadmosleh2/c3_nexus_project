from django.db import models
from django.utils.timezone import now
from django.conf import settings  
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('dealer', 'Dealer'),
        ('customer', 'Customer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return self.username

class AdminLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'User Logged In'),
        ('logout', 'User Logged Out'),
        ('claim_submitted', 'Claim Submitted'),
        ('inspection_submitted', 'Inspection Submitted'),
        ('admin_action', 'Admin Action'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(default=now)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()} - {self.timestamp}"




    def __str__(self):
        return f"Claim {self.id} - {self.status}"