from django.contrib import admin
from .models import Medicine, MedicationSchedule, Prescription

admin.site.register(Medicine)
admin.site.register(MedicationSchedule)
admin.site.register(Prescription)