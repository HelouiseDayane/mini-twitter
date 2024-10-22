from django.urls import path
from .views import UserCreateView, UserLoginView, UserDetailView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create-user'),
    path('login/', UserLoginView.as_view(), name='login-user'),
    path('me/', UserDetailView.as_view(), name='user-detail'), 
]