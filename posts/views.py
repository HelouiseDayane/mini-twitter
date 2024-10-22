from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like, Follow
from .serializers import PostSerializer, LikeSerializer, FollowSerializer
import logging
from rest_framework.decorators import api_view 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth import get_user_model
from .tasks import notify_followers


logger = logging.getLogger(__name__)
User = get_user_model()

class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        notify_followers.delay(post.id)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        logger.info("Post list retrieved")
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        logger.info(f"{self.__class__.__name__} created by {request.user.username}: {serializer.data}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class FollowCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer  

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        logger.info(f"Follow created by {request.user.username}: {serializer.data}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@method_decorator(cache_page(60 * 15), name='dispatch') 
class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            following_ids = user.following.values_list('following_id', flat=True)
            return Post.objects.filter(user_id__in=following_ids).order_by('-created_at')
        else:
            return Post.objects.all().order_by('?') 


@api_view(['POST'])
def create_follow(request):
    following_user_id = request.data.get('following')
    following_user = get_object_or_404(User, id=following_user_id)
    follow = Follow.objects.create(follower=request.user, following=following_user)
    return Response(status=status.HTTP_201_CREATED)