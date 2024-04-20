from django.core.exceptions import ValidationError
from django.core.validators import (FileExtensionValidator, MaxLengthValidator,
                                    RegexValidator, validate_slug)
from django.db import models
from django.utils import timezone

# Create your models here.

    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='blog_images/')
    image2 = models.ImageField(upload_to='blog_images/',default="")
    content1 = models.TextField()
    content2 = models.TextField(default="")
    created_at=models.DateTimeField(default=timezone.now)

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    image=models.ImageField(upload_to='testimonial_image/',default="")

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)