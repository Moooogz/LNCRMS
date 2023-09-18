from django.db import models

class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient_code=models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    bday = models.CharField(max_length=50,default='')
    civil_status = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    
class Medicinelist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

class Patienthistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    consultCounter = models.CharField(max_length=50)
    patient_code=models.CharField(max_length=50)
    remarks = models.CharField(max_length=500)

class Prescription(models.Model):
    created_at = models.DateField(auto_now_add=True)
    patient_code=models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    morning = models.CharField(max_length=50)
    noon = models.CharField(max_length=50)
    evening = models.CharField(max_length=50)


    