from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Medicinelist)
admin.site.register(Patienthistory)
admin.site.register(Prescription)
admin.site.register(PatientsAttachments)
admin.site.register(SystemLog)

