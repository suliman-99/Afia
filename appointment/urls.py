from rest_framework import routers
from appointment.views import *

router = routers.DefaultRouter()

router.register(
    'patient-create-appointment',
    PatientCreateAppointmentView,
    basename='patient-create-appointment'
)

router.register(
    'doctor-accept-appointment',
    DoctorAcceptAppointmentView,
    basename='doctor-accept-appointment'
)

router.register(
    'doctor-reject-appointment',
    DoctorRejectAppointmentView,
    basename='doctor-reject-appointment'
)

router.register(
    'patient-confirm-appointment',
    PatientConfirmAppointmentView,
    basename='patient-confirm-appointment'
)

router.register(
    'patient-cancel-appointment',
    PatientCancelAppointmentView,
    basename='patient-cancel-appointment'
)

urlpatterns = router.urls
