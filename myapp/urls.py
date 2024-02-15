from django.urls import path
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.home,name='home'),
    path('addHospital',views.addHospital,name='addHospital'),
    path('setHpswd/<str:hid>',views.setHpswd,name='setHpswd'),
    path('setHpswd/setHpswd/<str:hid>',views.setHpswd,name='setHpswd'),
    path('savepswd',views.savepswd,name='savepswd'),
    ]