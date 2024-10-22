from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Like, Follow, User
from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()

class PostTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")
        self.client.force_authenticate(user=self.user1)

    def test_create_post(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'Test Post',
            'content': 'This is a test post.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_list_posts(self):
        Post.objects.create(title='Test Post 1', content='Content 1', user=self.user1)
        Post.objects.create(title='Test Post 2', content='Content 2', user=self.user2)
        response = self.client.get(reverse('list_posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class LikeTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', user=self.user1)
        self.client.force_authenticate(user=self.user1)



class FollowTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')
        self.client.force_authenticate(user=self.user1)

    def test_create_follow(self):
        url = reverse('follow-create')  
        data = {
            'follower': self.user1.id,  
            'following': self.user2.id,  
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserFeedTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")
        self.user3 = User.objects.create_user(username="user3", password="password123")

        Follow.objects.create(follower=self.user1, following=self.user2)
        Follow.objects.create(follower=self.user1, following=self.user3)

        Post.objects.create(title='Post by User 2', content='Content 2', user=self.user2)
        Post.objects.create(title='Another Post by User 2', content='Another Content 2', user=self.user2)

    def test_user_feed_authenticated(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse('user_feed'))
        self.assertEqual(len(response.data), 4)

    def test_user_feed_unauthenticated(self):
        self.client.logout()  
        response = self.client.get(reverse('user_feed'))
        self.assertGreater(len(response.data), 0)  
