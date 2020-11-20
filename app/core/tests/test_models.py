from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@email.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        # These are the same as the assertions below. Not required for use.
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

        assert user.email == email
        assert user.check_password(password)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")

        assert user.email == email.lower()

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # Like e.g. `with pytest.raises(UserPermissionsError):` for pytest
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@email.com", "test123"
        )

        # Super user is included as part of the PermissionsMixin
        assert user.is_superuser
        assert user.is_staff
