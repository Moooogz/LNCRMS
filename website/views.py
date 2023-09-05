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
    return render(request, 'index.html',{})

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
       fName=request.POST['fName']
       mName=request.POST['mName']
       lName=request.POST['lName']
       age=request.POST['age']
       bday=request.POST['bday']
       civilstatus=request.POST['civilstatus']
       gender=request.POST['gender']
       address=request.POST['address']
       contactnum=request.POST['contactnum']              
       remarks=request.POST['remarks']

       datas = {}
       datas['first_name']=fName
       datas['middle_name']=mName
       datas['last_name']=lName
       datas['age']=age
       datas['bday']=bday
       datas['civil_status']=civilstatus
       datas['gender']=gender
       datas['address']=address
       datas['contact_number']=contactnum
       datas['remarks']=remarks
       newPatient = PatientForm(datas)
       newPatient.save()
    return redirect('home')

def process(request, obj_id):
    if os.path.exists('...'):
        messages.success(request, 'processed')