from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()  
        self.user = get_user_model().objects.create_user(username="user1", password="password123", email="user1@example.com")
        response = self.client.post(reverse('login-user'), {
            'username': 'user1',
            'password': 'password123'
        })
        self.token = response.data['access'] 

    def test_update_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token) 
        response = self.client.patch(reverse('user-detail'), {'username': 'updated_user1', 'email': 'updated_user1@example.com'})
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updated_user1')
        self.assertEqual(self.user.email, 'updated_user1@example.com')

    def test_update_user_invalid(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.patch(reverse('user-detail'), {'username': '', 'email': 'invalid_email'})
        self.assertEqual(response.status_code, 400)
