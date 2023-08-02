from rest_framework import serializers
from rest_framework.exceptions import NotFound
from Auth.response_templates import UserSerializer
from post.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'post_id']

    user = UserSerializer()
    post_id = serializers.CharField(write_only=True)

    def create(self, validated_data):
        post_id = validated_data.pop('post_id')

        try:
            validated_data['post'] = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound()
        
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'photo', 'user', 'comments']

    user = UserSerializer()
    comments = CommentSerializer(many=True)
        
