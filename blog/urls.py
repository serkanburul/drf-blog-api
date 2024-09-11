from django.urls import path
from .views import PostDetailAPIView, PostListCreateAPIView, CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list'),
    path('/<int:pk>', PostDetailAPIView.as_view(), name='post-detail'),
    path('/<int:post_id>/comments', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('/comments/<int:pk>', CommentDetailAPIView.as_view(), name='comment-detail'),
]
