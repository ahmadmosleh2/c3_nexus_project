from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Claim
from django.db.models import Q
from warranty.models import Claim

@login_required
def submit_claim(request):
    step = int(request.GET.get('step', 1))

    if request.method == 'POST':
        if step == 1:
            request.session['first_name'] = request.POST.get('first_name')
            request.session['last_name'] = request.POST.get('last_name')
            request.session['phone'] = request.POST.get('phone')
            request.session['email'] = request.POST.get('email')
            request.session['address'] = request.POST.get('address')
            request.session['address2'] = request.POST.get('address2')
            request.session['city'] = request.POST.get('city')
            request.session['province'] = request.POST.get('province')
            request.session['country'] = request.POST.get('country')
            request.session['postal_code'] = request.POST.get('postal_code')
            request.session['vehicle_make'] = request.POST.get('vehicle_make')
            request.session['vehicle_model'] = request.POST.get('vehicle_model')
            request.session['vehicle_year'] = request.POST.get('vehicle_year')
            return redirect('/claims/submit_claim/?step=2')


        elif step == 2:
            request.session['product'] = request.POST['product']
            request.session['dealership'] = request.POST['dealership']
            request.session['amount'] = request.POST['amount']
            request.session['description'] = request.POST['description']
            return redirect('/claims/submit_claim/?step=3')

        elif step == 3:
            Claim.objects.create(
                user=request.user,
                product=request.session['product'],
                dealership=request.session['dealership'],
                amount=request.session['amount'],
                status='submitted',
            )
            return redirect('claims')  # or your confirmation view

    return render(request, f"warranty/step{step}.html", {"step": step})


@login_required
def admin_review_claims(request):
    if not request.user.is_superuser:
        return redirect('home')  # Only admins can access
    claims = Claim.objects.all()
    return render(request, 'warranty/admin_review_claims.html', {'claims': claims})

def claims_overview(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    sort_by = request.GET.get('sort', '-last_updated')

    claims = Claim.objects.all()

    if search_query:
        claims = claims.filter(
            Q(dealership__icontains=search_query) |
            Q(product__icontains=search_query)
        )

    if status_filter:
        claims = claims.filter(status=status_filter)

    claims = claims.order_by(sort_by)

    return render(request, 'users/claims.html', {
        'claims': claims,
        'search_query': search_query,
        'status_filter': status_filter,
        'sort_by': sort_by,
    })


@login_required
def submit_claim_complete(request):
    return render(request, "warranty/submit_claim_complete.html")
    