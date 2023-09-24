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
        fields = ['medicine_name',
                  'dosage',                                
                ]
        

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_code',
                  'quantity',
                  'medicine_name',
                  'dosage',
                  'morning',
                  'noon',
                  'evening',                                
                ]

class PatienthistoryForm(ModelForm):
    class Meta:
        model = Patienthistory
        fields = [
                  'remarks',
                  'diagnosis',
                                              
                ]