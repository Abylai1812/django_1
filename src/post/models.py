import random 

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_actual = models.BooleanField(blank = True, null = True)
    categories = models.ManyToManyField("Category", related_name="posts")
    photo = models.ImageField(upload_to='post/imgs/', null=True)
    
    def __str__(self):
        return self.title