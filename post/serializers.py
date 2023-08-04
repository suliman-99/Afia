from rest_framework import serializers
from rest_framework.exceptions import NotFound
from Auth.response_templates import UserSerializer
from post.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'post_id', 'user', 'created_at']

    user = UserSerializer(read_only=True)
    post_id = serializers.CharField()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        post_id = validated_data.pop('post_id')
        try:
            validated_data['post'] = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound()
        
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'photo', 'user', 'comments', 'created_at']

    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
        
