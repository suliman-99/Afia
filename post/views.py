from rest_framework.viewsets import *
from rest_framework.mixins import *
from rest_framework import routers
from post.serializers import *


class PostViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.prefetch_related('comments').order_by('-created_at')


class CommentViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = CommentSerializer

