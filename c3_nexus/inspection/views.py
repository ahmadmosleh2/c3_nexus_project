from django.shortcuts import render

# Create your views here.
def submit_inspection(request):
    if request.method == 'POST':
        
        
        
        AdminLog.objects.create(user=request.user, action='inspection_submitted', details="User submitted an inspection.")

        return redirect('home')

    return render(request, 'inspection/submit_inspection.html')
