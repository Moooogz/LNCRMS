from django.urls import path
from . import views

urlpatterns = [
    path('patientlist',views.patientlist, name='patientlist'),
    path('', views.login_user, name='loginuser'),
    path('logout', views.logout_user, name='logoutuser'),
    path('patientinfo/<int:pk>', views.patientinfo, name='patientinfo'),
    path('medications/',views.medications, name='medications'),
    path('editmedicine/<int:pk>',views.editmedicine, name='editmedicine'),
   
]
