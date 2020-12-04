from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@email.com", password="testpass"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test that tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Cucumber"
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string respresentation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title="Steak and mushroom sauce",
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)
