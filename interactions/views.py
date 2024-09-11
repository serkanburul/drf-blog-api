from rest_framework import generics, permissions
from .models import Like, Dislike, Favorite
from .serializers import LikeSerializer, DislikeSerializer, FavoriteSerializer
from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly


# LIKE
class LikeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post = Post(id=self.kwargs.get('post_id'))
        return Like.objects.filter(post=post)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        user = self.request.user
        print(user)

        post = Post.objects.get(id=post_id)

        Dislike.objects.filter(post=post, user=user).delete()

        if not Like.objects.filter(post=post, user=user).exists():
            serializer.save(user=user, post=post)


class LikeDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


# DISLIKE
class DislikeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DislikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post = Post(id=self.kwargs.get('post_id'))
        return Dislike.objects.filter(post=post)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        user = self.request.user

        post = Post.objects.get(id=post_id)

        Like.objects.filter(post=post, user=user).delete()

        if not Dislike.objects.filter(post=post, user=user).exists():
            serializer.save(user=user, post=post)


class DislikeDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = DislikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Dislike.objects.filter(user=self.request.user)


# FAVORITE
class FavoriteCreateAPIView(generics.CreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        if not Favorite.objects.filter(post=post, user=self.request.user).exists():
            serializer.save(user=self.request.user, post=post)


class FavoriteDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)