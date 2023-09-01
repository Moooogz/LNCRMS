from django.shortcuts import render,redirect
from .models import Patient

def home(request):
    patientsdata = Patient.objects.all()
   
    return render(request, 'home.html',{'patientsdata': patientsdata})


def patientDetails(request):
    return render(request, 'patientdetails.html',{})