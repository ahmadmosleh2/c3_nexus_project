from django.shortcuts import render, redirect
from .models import Claim
from django.contrib.auth.decorators import login_required

@login_required
def submit_claim(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        claim = Claim.objects.create(user=request.user, description=description)
        return redirect('claim_success')
    return render(request, 'warranty/submit_claim.html')

@login_required
def admin_review_claims(request):
    if not request.user.is_superuser:
        return redirect('home')  # Only admins can access
    claims = Claim.objects.all()
    return render(request, 'warranty/admin_review_claims.html', {'claims': claims})

def claims_overview(request):
    claims = Claim.objects.all()  # Fetch all claims from the database
    return render(request, 'users/claims.html', {'claims': claims})