from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.permissions import IsAuthorOrReadOnly


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]



# COMMENTS
class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id is None:
            raise ValueError("post_id parameter is missing")
        return Comment.objects.filter(post_id=post_id, parent=None)

    def perform_create(self, serializer):
        parent_id = self.request.data.get('parent')
        post_id = self.kwargs.get('post_id')
        if parent_id:
            try:
                parent_comment = Comment.objects.get(id=parent_id)
                serializer.save(author=self.request.user, post_id=post_id, parent=parent_comment)
            except Comment.DoesNotExist:
                raise ValueError("Parent comment does not exist")
        else:
            serializer.save(author=self.request.user, post_id=post_id)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
