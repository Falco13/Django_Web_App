from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post, User


class PostSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['theme', 'content', 'create_date', 'user']


class UserSerializer(ModelSerializer):
    post_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'bio', 'date_of_birth', 'post_set']
