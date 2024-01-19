from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_code',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'age',
                  'bday',
                  'civil_status',
                  'gender',
                  'address',
                  'contact_number',   
                  'srID',
                  'pwdID',
                  'nationality',            
                ]
        
class PatientsAttachmentsForm(ModelForm):
    class Meta:
      model= PatientsAttachments
      fields = ['name',
                'fileattachments', 
      ]
        

class MedicineForm(ModelForm):
    class Meta:
        model = Medicinelist
        fields = ['medname',
                  'medgenname',
                  'medsize',                               
                ]
        

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_code',
                  'consultCounter',                  
                  'medname',
                  'medgenname',
                  'medsize',
                  'medqty',                                    
                  'medtype',
                  'perduration',
                  'durationqty',
                  'medduration',
                  'totalquantity',
                  'morning',
                  'noon',
                  'evening',                                
                ]

class PatienthistoryForm(ModelForm):
    class Meta:
        model = Patienthistory
        fields = ['bp',
                  'weight',
                  'height',
                  'bodytemp',
                  'remarks',
                  'diagnosis',
                  'objectives',
                  'plans_recommendations',
                                              
                ]