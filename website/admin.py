from django.contrib import admin
from .models import Patient,Medicinelist,Prescription,Patienthistory

admin.site.register(Patient)
admin.site.register(Medicinelist)
admin.site.register(Patienthistory)
admin.site.register(Prescription)
