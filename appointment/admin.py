from django.contrib import admin
from appointment.models import *


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

