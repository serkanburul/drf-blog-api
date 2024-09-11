from rest_framework import serializers
from jwt_auth.models import CustomUser
from blog.models import Post, Comment
from interactions.models import Like, Dislike, Favorite


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'biography', 'profile_picture' )


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_date', 'id', 'post']


class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'user', 'created_at')


class UserDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ('post', 'user', 'created_at')


class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('post', 'user', 'created_at')
