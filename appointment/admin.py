from django.contrib import admin
from appointment.models import *


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient', 'status', 'date', 'time', 'doctor_notes', 'patient_notes']

