from django.db import models
from django.contrib.auth import get_user_model
from static.models import Specialization


User = get_user_model()


class Consultation(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_consultations')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_consultations')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    symptoms = models.TextField()
    additional_explanation = models.TextField(null=True, blank=True)
    analysis = models.FileField(null=True, blank=True)
    done = models.BooleanField(default=False)

