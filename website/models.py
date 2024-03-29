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
    fileattachments = models.FileField(null=True, blank=True)
    atype = models.CharField(max_length=50,null=True, blank=True)
    
class Medicinelist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)   
    medname = models.CharField(max_length=100,null=True, blank=True)
    medgenname = models.CharField(max_length=50,null=True, blank=True)   
    medsize = models.CharField(max_length=50,null=True, blank=True) 

class Patienthistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    consultCounter = models.CharField(max_length=50)
    patient_code=models.CharField(max_length=50)
    diagnosis = models.TextField(default="*under observation",max_length=500,null=True, blank=True)
    remarks = models.TextField(default="*under observation",max_length=500,null=True, blank=True)
    objectives = models.TextField(default="*under observation",max_length=500,null=True, blank=True)
    plans_recommendations = models.TextField(default="*under observation",max_length=500,null=True, blank=True)
    bp = models.CharField(max_length=50,null=True, blank=True)
    weight = models.CharField(max_length=50,null=True, blank=True)
    height = models.CharField(max_length=50,null=True, blank=True)
    bodytemp = models.CharField(max_length=50,null=True, blank=True)

class Prescription(models.Model):
    created_at = models.DateField(auto_now_add=True)
    patient_code=models.CharField(max_length=50,null=True, blank=True)
    consultCounter = models.CharField(max_length=50,null=True, blank=True)
    medname = models.CharField(max_length=100,null=True, blank=True)
    medgenname = models.CharField(max_length=50,null=True, blank=True)   
    medsize = models.CharField(max_length=50,null=True, blank=True) 
    medqty = models.CharField(max_length=50,null=True, blank=True)
    medtype = models.CharField(max_length=50,null=True, blank=True)
    perduration = models.CharField(max_length=50,null=True, blank=True)
    durationqty = models.CharField(max_length=50,null=True, blank=True)
    medduration = models.CharField(max_length=50,null=True, blank=True)
    totalquantity = models.CharField(max_length=50,null=True, blank=True)
        
    dosage = models.CharField(max_length=50,null=True, blank=True)
    morning = models.CharField(max_length=50,null=True, blank=True)
    noon = models.CharField(max_length=50,null=True, blank=True)
    evening = models.CharField(max_length=50,null=True, blank=True)


class Dosageunit(models.Model):
    dosage_unit = models.CharField(max_length=50,null=True, blank=True)


class Dosageduration(models.Model):
    daysqty_duration = models.CharField(max_length=50,null=True, blank=True)
    dosage_duration = models.CharField(max_length=50,null=True, blank=True)


class SystemLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    userLog = models.CharField(max_length=50,null=True, blank=True)
    logMessage = models.CharField(max_length=200,null=True, blank=True)


class LabResults(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    labresultdate=models.CharField(max_length=50,null=True, blank=True)
    patient_code=models.CharField(max_length=50,null=True, blank=True)
    labname = models.CharField(max_length=50,null=True, blank=True)
    labresult = models.CharField(max_length=50,null=True, blank=True)
    labrange= models.CharField(max_length=50,null=True, blank=True)
    