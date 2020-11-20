from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    """User Manager class"""

    def create_user(self, email, password=None, **extra_fields):
        """
            Creates and saves a new user.
            Note: This removes the username required from the base user class.
        """
        if not email:
            raise ValueError('Users must have an email address')

        # Creates a new user with the following arguments.
        # normalize_email sets characters past `@` to be lower.
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Password is set seperately, so it is not done in clear text.
        user.set_password(password)

        # Saves the user in the db.
        # `using=_db` is used to support different databases.
        # `using=_db` is likely not required here.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using emails instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # I believe this is setting the query method
    objects = UserManager()

    # Names the username field as email
    USERNAME_FIELD = 'email'