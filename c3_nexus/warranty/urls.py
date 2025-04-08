from django.urls import path

from . import views




urlpatterns = [
    path('submit_claim/', views.submit_claim, name='submit_claim'),
    
    
]
