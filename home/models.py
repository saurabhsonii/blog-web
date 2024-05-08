from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
# Create your models here.

def custom_slugify(value):
    return value.replace(' ', '-')


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Required fields for user model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Category(models.Model):
    category_name = models.CharField(max_length=100,null=True)
    slug = AutoSlugField(populate_from=category_name, editable=True, slugify=custom_slugify)
    created_at = models.DateField(auto_created=True)

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="blog")
    title = models.CharField(max_length=200,null=True)
    slug = AutoSlugField(populate_from=title,editable=True,slugify=custom_slugify)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)
    bg_image = models.FileField(upload_to="media",null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name

class Comments(models.Model):
    message = models.TextField(null=True)

    def __str__(self):
        return self.message

class Subscribe(models.Model):
    subscribe_mail = models.EmailField(null=True)

    def __str__(self):
        return self.subscribe_mail