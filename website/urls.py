from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='loginuser'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('patienttable',views.patienttable, name='patienttable'),
    path('patientlist/',views.patientlist, name='patientlist'),
    path('deletepatient/<int:pk>',views.deletepatient, name='deletepatient'),
    path('editpatient/<int:pk>',views.editpatient, name='editpatient'),
    path('loginpage', views.login_user, name='loginuser'),
    path('logout', views.logout_user, name='logoutuser'),      
    path('registrationpage',views.registrationpage, name='registrationpage'),

    path('patientinfo/<int:pk>/prescription',views.prescription, name='prescription'),

    path('patientinfo/<int:pk>/medicalhistoryinfo/<int:pkHistory>',views.medicalhistoryinfo, name='medicalhistoryinfo'),
    path('patientinfo/<int:pk>/medicalhistoryinfo/<int:pkHistory>/<int:selectedmed>/',views.medicalhistoryinfo, name='medicalhistoryinfo'),

    path('patientinfo/<int:pk>/patientmedinfo_geninfo/<int:pkHistory>',views.patientmedinfo_geninfo, name='patientmedinfo_geninfo'),
    path('patientinfo/<int:pk>/patientmedinfo_geninfo/<int:pkHistory>/<int:selectedmed>/',views.patientmedinfo_geninfo, name='patientmedinfo_geninfo'),

    path('patientinfo/<int:pk>/patientmedinfo_medications/<int:pkHistory>',views.patientmedinfo_medications, name='patientmedinfo_medications'),
    path('patientinfo/<int:pk>/patientmedinfo_medications/<int:pkHistory>/<int:selectedmed>/',views.patientmedinfo_medications, name='patientmedinfo_medications'),
   
    path('patientinfo/<int:pk>/patientmedinfo_attachments/<int:pkHistory>',views.patientmedinfo_attachments, name='patientmedinfo_attachments'),
    path('patientinfo/<int:pk>/patientmedinfo_attachments/<int:pkHistory>/<int:selectedmed>/',views.patientmedinfo_attachments, name='patientmedinfo_attachments'),

    path('patientinfo/<int:pk>/medicalhistoryinfo/edit/<int:pkHistory>',views.editmedicalhistory, name='editmedicalhistory'),
    path('patientinfo/<int:pkpatient>/deletemedicalhistory/<int:pkmedhistory>',views.deletemedicalhistory, name='deletemedicalhistory'),

    path('patientinfo/<int:pk>', views.patientinfo, name='patientinfo'), 
    path('patientinfo/<int:pk>/<int:selectedmed>', views.patientinfo, name='patientinfo'), 
    
    path('patientinfo/<int:pk>/medicalhistorytb/',views.medicalhistorytb, name='medicalhistorytb'),
    path('medications/',views.medications, name='medications'),
    path('medications/<str:pk>',views.medications, name='medications'),
    path('editmedicine/<int:pk>',views.editmedicine, name='editmedicine'),
    path('updatemedrecord/<str:pk>',views.updatemedrecord, name='updatemedrecord'),
    path('deleteitemprescription/<int:pID>/<int:pk>/',views.deleteitemprescription, name='deleteitemprescription'),
    path('report/<int:pk>/<str:sig>/<str:conCounter>',views.pdfreport, name='report'),

    #delete attachments
    path('deleteattachment/<int:pID>/<str:pk>/<str:apk>/',views.deleteattachment, name='deleteattachment'),
]
