from django.urls import path
from appointment.views import *


urlpatterns = [
    path('patient-create-appointment/', PatientCreateAppointmentView.as_view(), name='patient-create-appointment'),
    path('doctor-accept-appointment/', DoctorAcceptAppointmentView.as_view(), name='doctor-accept-appointment'),
    path('doctor-reject-appointment/', DoctorRejectAppointmentView.as_view(), name='doctor-reject-appointment'),
    path('patient-confirm-appointment/', PatientConfirmAppointmentView.as_view(), name='patient-confirm-appointment'),
    path('patient-cancel-appointment/', PatientCancelAppointmentView.as_view(), name='patient-cancel-appointment'),
]

