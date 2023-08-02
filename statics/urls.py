from rest_framework import routers
from statics.views import *

router = routers.DefaultRouter()

router.register(
    'countries',
    CountryViewSet,
    basename='countries'
)

router.register(
    'cities',
    CityViewSet,
    basename='cities'
)

router.register(
    'specializations',
    SpecializationViewSet,
    basename='specializations'
)

urlpatterns = router.urls
