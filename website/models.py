from django.db import models

class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    bday = models.CharField(max_length=50,default='')
    civil_status = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    remarks = models.CharField(max_length=200)


class Medicinelist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    