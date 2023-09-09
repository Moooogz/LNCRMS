from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient
from .forms import PatientForm
import os

def home(request):        
    patientsdata = Patient.objects.all()
    return render(request, 'home.html',{'patientsdata': patientsdata})


def patientinfo(request,pk):
    patient_record = Patient.objects.get(id=pk)
    return render(request, 'patientinfo.html',{'patient_record':patient_record})

def patientlist(request):
    if request.method == 'POST':
       datas = {}
       datas['first_name']=request.POST['first_name']
       datas['middle_name']=request.POST['middle_name']
       datas['last_name']=request.POST['last_name']
       datas['age']=request.POST['age']
       datas['bday']=request.POST['bday']
       datas['civil_status']=request.POST['civil_status']
       datas['gender']=request.POST['gender']
       datas['address']=request.POST['address']
       datas['contact_number']=request.POST['contact_number']
       datas['remarks']=request.POST['remarks']
       newPatient = PatientForm(datas)
       newPatient.save()
       messages.success(request,"Added Patient Data Successfully")
       return redirect('patientlist')
    patientsdata = Patient.objects.all()
    return render(request, 'patientlist.html',{'patientsdata': patientsdata})

def login_user(request):
    if request.method == 'POST':
        uNmae = request.POST['uName']
        pWord = request.POST['pWord']

        user = authenticate(request, username=uNmae, password=pWord)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been login!")
            return redirect('patientlist')            
        else:
            messages.success(request,"Invalid Username and Password...")
            return render(request, 'login.html',{})
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    messages.success(request,"You logout successfully")
    logout(request)
    return redirect('loginuser')


