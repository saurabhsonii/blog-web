from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    pass

def custom_slugify(value):
    return value.replace(' ', '-')
class Blog(models.Model):
    title = models.CharField(max_length=100,null=True)
    slug = AutoSlugField(populate_from=title,editable=True,slugify=custom_slugify)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)


    def __str__(self):
        return self.title