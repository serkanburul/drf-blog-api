from .permissions import is_author
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from jwt_auth.models import CustomUser
from blog.models import Post, Comment
from interactions.models import Like, Dislike, Favorite
from .serializers import UserSerializer, UserPostSerializer, UserCommentSerializer, UserLikeSerializer, UserDislikeSerializer, UserFavoriteSerializer


class UserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)


class UserPostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = UserPostSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user_id = CustomUser.objects.filter(username=username).values_list('id', flat=True).first()
        return self.queryset.filter(author_id=user_id)


class UserCommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = UserCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        user_id = CustomUser.objects.get(username=username)
        return self.queryset.filter(author_id=user_id)


class UserLikeListView(generics.ListAPIView):
    serializer_class = UserLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if is_author(self, CustomUser):
            queryset = Like.objects.filter(user=self.request.user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, content_type='application/json')
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'Authentication credentials were not provided.'})


class UserDislikeListView(generics.ListAPIView):
    serializer_class = UserDislikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if is_author(self, CustomUser):
            queryset = Dislike.objects.filter(user=self.request.user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, content_type='application/json')
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'Authentication credentials were not provided.'})


class UserFavoriteListView(generics.ListAPIView):
    serializer_class = UserFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if is_author(self, CustomUser):
            queryset = Favorite.objects.filter(user=self.request.user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, content_type='application/json')
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'Authentication credentials were not provided.'})


class UserEditUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ['PATCH']

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)

    def patch(self, request, *args, **kwargs):
        if is_author(self, CustomUser):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'Authentication credentials were not provided.'})
