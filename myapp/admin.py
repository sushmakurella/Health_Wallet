from django.contrib import admin
from .models import Patient,Hospital,DiagCenter,PatientDetails,pdfs,image,Pres
# Register your models here.
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(DiagCenter)
admin.site.register(PatientDetails)
admin.site.register(pdfs)
admin.site.register(image)
admin.site.register(Pres)
