# users/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'password'] 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()  
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password', None)
        return representation

    def get_posts(self, obj):
        from posts.serializers import PostSerializer  
        posts = obj.posts.all() 
        return PostSerializer(posts, many=True).data

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise ValidationError("Credenciais inválidas")
        return user

def update(self, instance, validated_data):
    instance.username = validated_data.get('username', instance.username)
    instance.email = validated_data.get('email', instance.email)
    if 'password' in validated_data:
        instance.set_password(validated_data['password']) 
    instance.save()
    return instance

