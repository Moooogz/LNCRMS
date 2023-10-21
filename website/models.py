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
    srID = models.CharField(max_length=50,null=True, blank=True)
    pwdID = models.CharField(max_length=50,null=True, blank=True)
    nationality = models.CharField(max_length=50,null=True, blank=True)
    
    def __str__(self):
        return self.patient_code
   
    
    
class PatientsAttachments(models.Model):
    patient_code=models.CharField(max_length=50,null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    consultCounter = models.CharField(max_length=50,null=True, blank=True)
    fileattachments = models.ImageField(null=True, blank=True)
    
class Medicinelist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

class Patienthistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    consultCounter = models.CharField(max_length=50)
    patient_code=models.CharField(max_length=50)
    diagnosis = models.TextField(default="*under observation",max_length=500,null=True, blank=True)
    remarks = models.TextField(max_length=500,null=True, blank=True)
    objectives = models.TextField(max_length=500,null=True, blank=True)
    plans_recommendations = models.TextField(max_length=500,null=True, blank=True)
    bp = models.CharField(max_length=50,null=True, blank=True)

class Prescription(models.Model):
    created_at = models.DateField(auto_now_add=True)
    patient_code=models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    morning = models.CharField(max_length=50)
    noon = models.CharField(max_length=50)
    evening = models.CharField(max_length=50)


    