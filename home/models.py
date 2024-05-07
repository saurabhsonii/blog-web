from django.db import models
from autoslug import AutoSlugField
# Create your models here.

def custom_slugify(value):
    return value.replace(' ', '-')

# class User(models.Model):
#     user = models
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

class Commnets(models.Model):
    message = models.TextField(null=True)

    def __str__(self):
        return self.message

class Subcribe(models.Model):
    subscribe_mail = models.EmailField(null=True)

    def __str__(self):
        return self.subscribe_mail