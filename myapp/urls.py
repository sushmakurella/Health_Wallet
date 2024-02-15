from django.urls import path
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.home,name='home'),
    path('addHospital',views.addHospital,name='addHospital'),
    path('addDiag',views.addDiag, name = 'addDiag'),
    path('setHpswd/<str:hid>',views.setHpswd,name='setHpswd'),
    path('setHpswd/setHpswd/<str:hid>',views.setHpswd,name='setHpswd'),
    path('setDpswd/<str:did>',views.setDpswd,name='setDpswd'),
    path('setDpswd/setDpswd/<str:did>',views.setDpswd,name='setDpswd'),
    
    path('savepswd',views.savepswd,name='savepswd'),
    path('hospitallogin',views.hospitalLogin,name='hospitallogin'),
    path('patientRegister',views.patientRegister,name='patientRegister'),

    path('diaglogin', views.diaglogin, name='diaglogin'),
    
    ]