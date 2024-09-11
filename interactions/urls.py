from django.urls import path
from .views import LikeListCreateAPIView, LikeDetailView, DislikeListCreateAPIView, DislikeDetailView, \
    FavoriteCreateAPIView, FavoriteDetailView

urlpatterns = [
    path('like/post/<int:post_id>', LikeListCreateAPIView.as_view(), name='like-list-create'),
    path('like/<int:pk>', LikeDetailView.as_view(), name='like-detail'),
    path('dislike/post/<int:post_id>', DislikeListCreateAPIView.as_view(), name='dislike-list-create'),
    path('dislike/<int:pk>', DislikeDetailView.as_view(), name='dislike-detail'),
    path('favorite/post/<int:post_id>', FavoriteCreateAPIView.as_view(), name='favorite-list-create'),
    path('favorite/<int:pk>', FavoriteDetailView.as_view(), name='favorite-detail'),
]
