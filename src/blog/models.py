from django.db import models

# Create your models here.

# Don't forget three things for CHANGES TO THIS FILE:
# 1. Make sure the app is in your settings
# 2. python manage.py makemigrations
# 3. python manage.py migrate


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
