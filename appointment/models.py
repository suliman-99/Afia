from django.db import models
from Auth.models import User


class Appointment(models.Model):
    STATUS_REQUESTED = 0
    STATUS_ACCEPTED = 1
    STATUS_REJECTED = 2
    STATUS_CONFIRMED = 3
    STATUS_CANCELED = 4

    STATUS_CHOICES = (
        (STATUS_REQUESTED, 'Requested'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELED, 'Canceled'),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_REQUESTED)
    date = models.DateField(null=True, blank=True)
    suggested_date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    patient_notes = models.TextField(null=True, blank=True)
    doctor_notes = models.TextField(null=True, blank=True)

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')



