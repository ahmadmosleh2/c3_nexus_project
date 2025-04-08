from django import forms
from .models import Claim

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['dealership', 'product', 'amount']
