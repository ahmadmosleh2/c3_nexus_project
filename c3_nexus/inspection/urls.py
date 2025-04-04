from django.urls import path
from .views import submit_inspection

urlpatterns = [
    path('submit_inspection/', submit_inspection, name='submit_inspection'),
]
