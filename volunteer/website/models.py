from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class University(models.Model):
    name = models.TextField(primary_key=True)
    def __str__(self):
        return self.name

class Profile(AbstractUser):
    email=models.CharField(primary_key=True,max_length=155)
    phone_number=models.CharField(max_length=10)
    university = models.ManyToManyField(University)
    profile_picture = models.ImageField(upload_to='pictures/')
    REQUIRED_FIELDS=['email', 'phone_number', 'first_name', 'last_name', 'university', 'profile_picture',]

    def __str__(self):
        return self.email

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    lastModified = models.DateTimeField(auto_now=True)
    organization = models.CharField(max_length=50)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name