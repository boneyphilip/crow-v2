import json

from django.test import TestCase
from django.urls import reverse


class PostViewsTests(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        from .models import Post

        self.author = User.objects.create_user(
            username="author",
            password="StrongPass123!",
        )
        self.other_user = User.objects.create_user(
            username="otheruser",
            password="StrongPass123!",
        )
        self.post = Post.objects.create(
            author=self.author,
            title="Test Post",
            content="This is test content.",
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_create_post_requires_login(self):
        response = self.client.get(reverse("create_post"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_authenticated_user_can_create_post(self):
        from .models import Post

        self.client.login(username="author", password="StrongPass123!")

        response = self.client.post(
            reverse("create_post"),
            {
                "title": "Created Post",
                "content": "Created content",
                "category": "testing",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Created Post").exists())

    def test_author_can_edit_own_post(self):
        self.client.login(username="author", password="StrongPass123!")

        response = self.client.post(
            reverse("edit_post", args=[self.post.id]),
            {
                "title": "Updated Title",
                "content": "Updated content",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Title")

    def test_non_author_cannot_edit_post(self):
        self.client.login(username="otheruser", password="StrongPass123!")

        response = self.client.get(reverse("edit_post", args=[self.post.id]))
        self.assertEqual(response.status_code, 403)

    def test_author_can_delete_own_post(self):
        from .models import Post

        self.client.login(username="author", password="StrongPass123!")

        response = self.client.post(reverse("delete_post", args=[self.post.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_authenticated_user_can_add_comment(self):
        from .models import Comment

        self.client.login(username="author", password="StrongPass123!")

        response = self.client.post(
            reverse("add_comment", args=[self.post.id]),
            {"content": "New comment"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Comment.objects.filter(
                post=self.post,
                content="New comment",
            ).exists()
        )

    def test_user_can_vote_on_post(self):
        from .models import Vote

        self.client.login(username="author", password="StrongPass123!")

        response = self.client.post(
            reverse("vote_post", args=[self.post.id]),
            data=json.dumps({"action": "upvote"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Vote.objects.filter(
                post=self.post,
                user=self.author,
            ).exists()
        )

    def test_ajax_search_returns_matching_post(self):
        response = self.client.get(
            reverse("ajax_search"),
            {"q": "Test"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_profile_page_loads(self):
        response = self.client.get(
            reverse("profile_page", args=[self.author.username])
        )
        self.assertEqual(response.status_code, 200)
