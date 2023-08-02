from django.db import models
from django.contrib.auth import get_user_model
from statics.models import Specialization


User = get_user_model()


class Consultation(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_consultations')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_consultations')
    symptoms = models.TextField()

    additional_explanation = models.TextField(null=True, blank=True)
    analysis = models.FileField(null=True, blank=True)

    diagnosis = models.TextField()
    prescription = models.TextField()
    treatment_duration = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


class Review(models.Model):
    
    REQUESTER_DOCTOR = 0
    REQUESTER_PATIENT = 1

    REQUESTER_CHOICES = (
        (REQUESTER_DOCTOR, 'Doctor'),
        (REQUESTER_PATIENT, 'patient'),
    )

    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='reviews')
    review_reasons = models.TextField()
    requester = models.IntegerField(choices=REQUESTER_CHOICES)

    additional_explanation = models.TextField(null=True, blank=True)
    analysis = models.FileField(null=True, blank=True)

    diagnosis = models.TextField()
    prescription = models.TextField()
    treatment_duration = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

