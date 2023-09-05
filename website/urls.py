from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage, name='indexpage'),
    path('patientdetails/',views.patientDetails, name='patientdetails'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('login/', views.login_user, name='loginuser'),
   
]
