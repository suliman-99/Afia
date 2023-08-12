from django.urls import path
from appointment.views import *


urlpatterns = [
    path('patient-create-appointment/', PatientCreateAppointmentView.as_view(), name='patient-create-appointment'),
    path('doctor-accept-appointment/<pk>/', DoctorAcceptAppointmentView.as_view(), name='doctor-accept-appointment'),
    path('doctor-reject-appointment/<pk>/', DoctorRejectAppointmentView.as_view(), name='doctor-reject-appointment'),
    path('patient-request-appointment/<pk>/', PatientRequestAppointmentView.as_view(), name='patient-request-appointment'),
    path('patient-confirm-appointment/<pk>/', PatientConfirmAppointmentView.as_view(), name='patient-confirm-appointment'),
    path('patient-cancel-appointment/<pk>/', PatientCancelAppointmentView.as_view(), name='patient-cancel-appointment'),
    path('appointments/', AppointmentView.as_view(), name='appointments'),
]

