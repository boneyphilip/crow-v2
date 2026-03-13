from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountViewsTests(TestCase):
    def test_register_page_loads(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_user_can_register(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_can_log_in(self):
        User.objects.create_user(
            username="testuser",
            password="StrongPass123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
