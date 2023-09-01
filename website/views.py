from django.shortcuts import render
from .models import Patient

def home(request):
    patientsdata = Patient.objects.all()
   
    return render(request, 'home.html',{'patientsdata': patientsdata})
