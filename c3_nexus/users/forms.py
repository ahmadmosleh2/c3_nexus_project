from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  
from .models import Claim



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'email', 'password1', 'password2', 'role']  # Adjust fields as needed


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['product', 'amount']