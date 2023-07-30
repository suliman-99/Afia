from rest_framework.routers import DefaultRouter
from user_profile.views import *

router = DefaultRouter()

router.register(
    'patient-profiles',
    PatientProfileViewSet,
    basename='patient-profiles'
)

router.register(
    'doctor-profiles',
    DoctorProfileViewSet,
    basename='doctor-profiles'
)

urlpatterns = router.urls