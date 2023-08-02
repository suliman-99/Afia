from rest_framework import routers
from post.views import *

router = routers.DefaultRouter()

router.register(
    'posts',
    PostViewSet,
    basename='posts'
)

router.register(
    'comments',
    PostViewSet,
    basename='comments'
)

urlpatterns = router.urls
