from rest_framework import serializers
from .models import Post, Like, Follow
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'created_at']
        extra_kwargs = {'user': {'read_only': True}}

    def get_user(self, obj):
        from users.serializers import UserSerializer  
        return UserSerializer(obj.user).data  

    def get_like_count(self, obj):
        return obj.like_set.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        extra_kwargs = {'user': {'read_only': True}}
    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Post não encontrado.")
        return value


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        extra_kwargs = {'follower': {'required': True}, 'following': {'required': True}}
    def validate(self, data):
        if data['follower'] == data['following']:
            raise serializers.ValidationError("Você não pode seguir a si mesmo.")
        return data