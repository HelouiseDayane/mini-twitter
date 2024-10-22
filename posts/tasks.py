from celery import shared_task
from django.contrib.auth.models import User
from .models import Post

@shared_task
def notify_followers(post_id):
    post = Post.objects.get(id=post_id)
    followers = post.user.followers.all() 

    for follower in followers:
        print(f'Notificando {follower.username} sobre o novo post de {post.user.username}')
