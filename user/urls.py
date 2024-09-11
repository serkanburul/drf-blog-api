from django.urls import path
from user.views import UserPostListView, UserView, UserLikeListView, UserDislikeListView, \
    UserFavoriteListView, UserCommentListView, UserEditUpdateView

urlpatterns = [
    path('<str:username>', UserView.as_view(), name='user'),
    path('<str:username>/posts', UserPostListView.as_view(), name='user_detail'),
    path('<str:username>/comments', UserCommentListView.as_view(), name='user_comments'),
    path('<str:username>/likes', UserLikeListView.as_view(), name='user_like'),
    path('<str:username>/dislikes', UserDislikeListView.as_view(), name='user_dislike'),
    path('<str:username>/favorites', UserFavoriteListView.as_view(), name='user_like'),
    path('<str:username>/edit', UserEditUpdateView.as_view(), name='user_edit' ),
]
