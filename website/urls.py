from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('patientdetails/',views.patientDetails, name='patientdetails'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('login/', views.login_user, name='loginuser'),
   
]
