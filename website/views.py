from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient
from .forms import PatientForm
import os

def home(request):        
    patientsdata = Patient.objects.all()
    return render(request, 'home.html',{'patientsdata': patientsdata})


def patientDetails(request):
    return render(request, 'patientdetails.html',{})

def indexpage(request):
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
       return redirect('indexpage')
    patientsdata = Patient.objects.all()
    return render(request, 'index.html',{'patientsdata': patientsdata})

def login_user(request):
    if request.method == 'POST':
        uNmae = request.POST['uName']
        pWord = request.POST['pWord']

        user = authenticate(request, username=uNmae, password=pWord)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been login!")
            return redirect('home')            
        else:
            messages.success(request,"Invalid Username and Password...")
            return render(request, 'login.html',{})
    else:
        return render(request, 'login.html',{})

def addpatient(request):
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
    return redirect('indexpage')

def process(request, obj_id):
    if os.path.exists('...'):
        messages.success(request, 'processed')