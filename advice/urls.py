from rest_framework import routers
from advice.views import *

router = routers.DefaultRouter()

router.register(
    'advices',
    AdviceViewSet,
    basename='advices'
)

urlpatterns = router.urls
