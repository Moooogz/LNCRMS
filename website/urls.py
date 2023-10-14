from django.urls import path
from . import views

urlpatterns = [
    path('patientlist/',views.patientlist, name='patientlist'),
    path('deletepatient/<int:pk>',views.deletepatient, name='deletepatient'),
    path('', views.login_user, name='loginuser'),
    path('logout', views.logout_user, name='logoutuser'),      
    path('patientinfo/<int:pk>/medicalhistoryinfo/<int:pkHistory>',views.medicalhistoryinfo, name='medicalhistoryinfo'),
    path('patientinfo/<int:pk>', views.patientinfo, name='patientinfo'), 
    path('patientinfo/<int:pk>/medicalhistorytb/',views.medicalhistorytb, name='medicalhistorytb'),
    path('medications/',views.medications, name='medications'),
    path('medications/<str:pk>',views.medications, name='medications'),
    path('editmedicine/<int:pk>',views.editmedicine, name='editmedicine'),
    path('updatemedrecord/<str:pk>',views.updatemedrecord, name='updatemedrecord'),
    path('deleteitemprescription/<int:pID>/<int:pk>/',views.deleteitemprescription, name='deleteitemprescription'),
    path('report/<int:pk>/',views.pdfreport, name='report'),
]
