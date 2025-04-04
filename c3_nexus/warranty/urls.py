from django.urls import path
from .views import submit_claim  # Ensure the view exists

urlpatterns = [
    path('submit_claim/', submit_claim, name='submit_claim'),
]
