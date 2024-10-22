from django.urls import path
from .views import PostCreateView, PostListView, LikeCreateView, FollowCreateView, UserFeedView

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='create_post'),
    path('posts/', PostListView.as_view(), name='list_posts'),
    path('likes/create/', LikeCreateView.as_view(), name='create_like'),
    path('follows/', FollowCreateView.as_view(), name='follow-create'),
    path('user/feed/', UserFeedView.as_view(), name='user_feed'),
]