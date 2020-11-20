from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """Setup function"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@email.com",
            password="password123"
        )
        # logs the user in
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@email.com",
            password="password123",
            name="Test user"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        # get request
        response = self.client.get(url)

        # assertContains() checks for 200 response, and the contents
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        assert res.status_code == 200

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        assert res.status_code == 200
