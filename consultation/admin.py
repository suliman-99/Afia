from django.contrib import admin
from consultation.models import *


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient', 'need_review_at', 'created_at', 'done']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient', 'need_review_at', 'created_at', 'done']

    def doctor(self, review):
        return review.consultation.doctor

    def patient(self, review):
        return review.consultation.patient
