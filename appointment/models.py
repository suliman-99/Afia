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
    date = models.DateField()
    time = models.TimeField()
    patient_notes = models.TextField()
    doctor_notes = models.TextField()

    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')



