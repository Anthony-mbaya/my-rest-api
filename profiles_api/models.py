from django.db import models
#key classes used to customize and
# extend the default user mode
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings



class UserProfileManager(BaseUserManager):
    """Manager for our user profiles"""
    def create_user(self, email, name, password=None):
        """creating a new user profile"""
        if not email:
            raise ValueError('User must have a valid email')
        #This converts the email to a normalized format (e.g., converting the domain part to lowercase).
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        #use this to ensure password is hidden in # encrypt
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create a new superuser"""
        user = self.create_user(email, name, password)


        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrive short name"""
        return self.name

    def __str__(self):
        """return string rep of the user"""
        return self.email



class ProfileFeedItem(models.Model):
    """profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return models as string"""
        return self.status_text





# Create your models here.
