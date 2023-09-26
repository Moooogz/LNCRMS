from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
import os

def consultCounter():
    counter = "0"
    if Patienthistory.objects.all().count()==0:
        counter="1"
    else:
        counter=int(Patienthistory.objects.latest('id').consultCounter)+1
    return counter

def patientinfoData(pk):
    medicines_list = Medicinelist.objects.all()   
    patient_record = Patient.objects.get(id=pk)
    medicationrecord = Prescription.objects.filter(patient_code=patient_record.patient_code)
    context = { 'medicationrecord': medicationrecord,
               'patient_record':patient_record,
               'medicines_list':medicines_list,
               'pID':pk,
               }
    return context


def home(request):        
    patientsdata = Patient.objects.all()
    return render(request, 'home.html',{'patientsdata': patientsdata})

def medicalhistorytb(request,pk):
    context = patientinfoData(pk)
    pCode=patientinfoData(pk)['patient_record'].patient_code
    form =PatientsAttachmentsForm()
    pHistoryForm = PatienthistoryForm()
    
    if request.method=='POST':
        pHistoryForm = PatienthistoryForm(request.POST,request.FILES)
        form = PatientsAttachmentsForm(request.POST,request.FILES)
        # if form.is_valid():
        #     a=form.save(commit=False)
        #     a.patient_code = patient_record.patient_code
        #     a.save()
        if pHistoryForm.is_valid():
            pHistoryForm_final = pHistoryForm.save(commit=False)
            pHistoryForm_final.consultCounter = str(consultCounter())
            pHistoryForm_final.patient_code = pCode
            pHistoryForm_final.save()
            print("success")
        else:
            print("error")
    context['form']=form
    context['pHistoryForm']=pHistoryForm
   
    return render(request,'tables/medicalhistorytb.html',context)    

def medicalhistoryinfo(request,pk,pkHistory):
    
    context=patientinfoData(pk)
    context['patient_history']= Patienthistory.objects.get(id=pkHistory)
    

    return render(request,'medicalhistoryinfo.html',context) 


def patientinfo(request,pk):
    
    context = patientinfoData(pk)
    pCode=patientinfoData(pk)['patient_record'].patient_code
    if 'addtoprescription' in request.POST:
        newPrescriptionData={}        
        newPrescriptionData['patient_code'] = pCode
        newPrescriptionData['quantity']=request.POST['qtyvalue']
        newPrescriptionData['medicine_name']=request.POST['medName']
        newPrescriptionData['dosage'] =request.POST['dosage']
        newPrescriptionData['morning'] =request.POST['am']
        newPrescriptionData['noon'] =request.POST['noon']
        newPrescriptionData['evening'] =request.POST['pmvalue']
        newPrescription = PrescriptionForm(newPrescriptionData)
        newPrescription.save()
    return render(request, 'patientinfo.html',context)

def deleteitemprescription(request,pID,pk):
    PrescriptionItem= Prescription.objects.get(id=pk)
    PrescriptionItem.delete()
    return redirect(f'/patientinfo/{pID}')
    
    
def patientlist(request):
    if request.method == 'POST':
       phistory={}
       datas = {}
       if Patient.objects.all().count()==0:
           datas['patient_code']='P-001'
           phistory['patient_code']='P-001'
       else:       
           lastcode=int(Patient.objects.latest('id').patient_code.split('-')[1])
           lastcode= lastcode+1
           datas['patient_code']=f"P-{lastcode:03}"
           phistory['patient_code']=f"P-{lastcode:03}"           
       datas['first_name']=request.POST['first_name']
       datas['middle_name']=request.POST['middle_name']
       datas['last_name']=request.POST['last_name']
       datas['age']=request.POST['age']
       datas['bday']=request.POST['bday']
       datas['civil_status']=request.POST['civil_status']
       datas['gender']=request.POST['gender']
       datas['address']=request.POST['address']
       datas['contact_number']=request.POST['contact_number']
       phistory['remarks']=request.POST['remarks']
       phistory['consultCounter']=str(consultCounter())
       
        

       #patienttable
       newPatient = PatientForm(datas)
       newPatient.save()

       #PatienthistoryTable
       newPatienthistory = PatienthistoryForm(phistory)
       newPatienthistory.save()

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