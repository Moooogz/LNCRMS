from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient,Medicinelist
from .forms import PatientForm,MedicineForm
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
       if Patient.objects.all().count()==0:
           datas['patient_code']='P-001'
       else:       
           lastcode=int(Patient.objects.latest('id').patient_code.split('-')[1])
           lastcode= lastcode+1
           datas['patient_code']=f"P-{lastcode:03}"
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
    patientsdata = {'patientsdata': Patient.objects.all()}
    return render(request, 'patientlist.html',patientsdata)

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

def medications(request,pk=''):
    

    if 'save' in request.POST:
       medData = {}
       medData['medicine_name']=request.POST['medname']
       medData['dosage']=request.POST['dosage']       
       newMedicine = MedicineForm(medData)
       newMedicine.save()
       messages.success(request,"Added Medicine Successfully")
       return redirect('medications')
       
      
    
    elif 'update'in request.POST: 
        editrecord = Medicinelist.objects.get(id=pk)
        medName=request.POST.get(f'medname{pk}',False)
        medDosage=request.POST.get(f'dosage{pk}',False)
        editrecord.medicine_name=medName
        editrecord.dosage=medDosage
        editrecord.save()
        return redirect('medications')
        messages.success(request,"Record Updated")
    elif 'delete'in request.POST:
        editrecord = Medicinelist.objects.get(id=pk)
        editrecord.delete()
        messages.success(request,"Record Deleted")
        return redirect('medications')
    medicinedata ={'medicinedata': Medicinelist.objects.all()}
    return render(request, 'medications.html',medicinedata)

def editmedicine(request,pk):
    medicine_record = Medicinelist.objects.get(id=pk)
    return render(request, 'editmedicine.html',{'medicine_record':medicine_record})


def updatemedrecord(request,pk):
    # editrecord = Medicinelist.objects.get(id=pk)
    # editrecord.medicine_name=request.POST[f"medname{pk}"]
    # editrecord.dosage=request.POST[f"dosage{pk}"]
    # editrecord.save()
    mednameDict = request.GET.get('update',1)

    messages.success(request,mednameDict)  
    return redirect('medications')