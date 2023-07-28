from rest_framework import routers
from seeding.views import *

router = routers.DefaultRouter()

router.register(
    'applied-seeders',
    AppliedSeederViewSet,
    basename='applied-seeders'
)

urlpatterns = router.urls
