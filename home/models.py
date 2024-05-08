from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

def custom_slugify(value):
    return value.replace(' ', '-')


class Role(models.Model):
    """
    Represents user roles and permissions.
    """
    name = models.CharField(max_length=100)
    permissions = models.TextField()

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """
    Custom user manager to handle user creation.
    """

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with additional fields such as roles.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')  # Foreign key to Role model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

### 2. **Post Model (`Post`)**

class Post(models.Model):
    """
    Represents blog posts in the application.
    """
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=title, unique=True,slugify=custom_slugify)  # URL-friendly slug derived from title
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Foreign key to User model
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,
                                 related_name='posts')  # Foreign key to Category model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

### 3. **Comment Model (`Comment`)**

class Comment(models.Model):
    """
    Represents comments on blog posts.
    """
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Foreign key to Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Foreign key to User model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


### 4. **Category Model (`Category`)**
class Category(models.Model):
    """
    Represents categories for blog posts.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=name, unique=True,slugify=custom_slugify)  # URL-friendly slug derived from name
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


### 5. **Tag Model (`Tag`)**

class Tag(models.Model):
    """
    Represents tags for blog posts.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from=name, unique=True,slugify=custom_slugify)  # URL-friendly slug derived from name

    def __str__(self):
        return self.name


### 6. **Post-Tag Association Model (`PostTag`)**
class PostTag(models.Model):
    """
    Represents the many-to-many relationship between posts and tags.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')  # Foreign key to Post model
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_posts')  # Foreign key to Tag model

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"


### 7. **Like Model (`Like`)**
class Like(models.Model):
    """
    Represents likes for blog posts.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')  # Foreign key to Post model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')  # Foreign key to User model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.title}"



### 8. **Follow Model (`Follow`)**

class Follow(models.Model):
    """
    Represents follows between users.
    """
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')  # Foreign key to User model
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')  # Foreign key to User model

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


