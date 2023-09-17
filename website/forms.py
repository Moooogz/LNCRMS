from django.forms import ModelForm
from .models import Patient,Medicinelist

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
                  'remarks',                
                ]
        

class MedicineForm(ModelForm):
    class Meta:
        model = Medicinelist
        fields = ['medicine_name',
                  'dosage',                                
                ]