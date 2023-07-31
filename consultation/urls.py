from rest_framework import routers
from consultation.views import *

router = routers.DefaultRouter()

router.register(
    'consultations',
    ConsultationViewSet,
    basename='consultations'
)

router.register(
    'reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = router.urls
